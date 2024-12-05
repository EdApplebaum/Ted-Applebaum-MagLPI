/*
 * Block_Driver.h
 *
 *  Created on: Nov 19, 2024
 *      Author: 14408
 */

#ifndef INC_BLOCK_DRIVER_H_
#define INC_BLOCK_DRIVER_H_

typedef struct {
	uint16_t x;
	uint16_t y;
}Coord_t;

typedef struct{
	Coord_t blocks[7];
}Shape;

static Shape active;
static Coord_t base[100];

const Coord_t

void CreateShape();
void StopShape();
void RotateShape();
void ShapeFall();

#endif /* INC_BLOCK_DRIVER_H_ */
