using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Teleport : MonoBehaviour
{
    private Vector2 screenBounds;
    private float objectWidth;
    private float objectHeight;

    private void OnEnable()
    {
        screenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));
        //For sprites, substitute SpriteRenderer for MeshRenderer
        objectWidth = transform.GetComponent<MeshRenderer>().bounds.size.x / 2;
        objectHeight = transform.GetComponent<MeshRenderer>().bounds.size.y / 2;

        Respawn();
    }

    // Update is called once per frame
    void Update()
    {
        if (transform.position.y < (screenBounds.y * -1 - objectHeight)-10)
        {
            Respawn();
        }
    }

    void Respawn()
    {
        float randomX = UnityEngine.Random.Range(screenBounds.x + objectWidth, screenBounds.x * -1 - objectWidth);
        float randomY = UnityEngine.Random.Range((screenBounds.y + objectHeight) + 10, (screenBounds.y + objectHeight) + 20);

        transform.position = new Vector3(randomX, randomY);
        var rigidbody = GetComponent<Rigidbody>();
        rigidbody.velocity = Vector3.zero;
    }
}
