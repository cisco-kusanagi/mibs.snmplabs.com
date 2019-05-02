#
# PySNMP MIB module SAMSUNG-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:00:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, Gauge32, MibIdentifier, ObjectIdentity, Integer32, Counter64, NotificationType, IpAddress, Unsigned32, ModuleIdentity, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "Gauge32", "MibIdentifier", "ObjectIdentity", "Integer32", "Counter64", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "Counter32", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
samsung = ModuleIdentity((1, 3, 6, 1, 4, 1, 236))
if mibBuilder.loadTexts: samsung.setLastUpdated('0209170000Z')
if mibBuilder.loadTexts: samsung.setOrganization('Samsung Corporation - Samsung DPD Solution SW Team')
if mibBuilder.loadTexts: samsung.setContactInfo(' SCMI Editors Samsung DPD Solution SW Team ')
if mibBuilder.loadTexts: samsung.setDescription('Samsung Printer Common MIB Root Module, Version 1.00. Copyright (C) 2003-2004 Samsung Corporation. All Rights Reserved.')
division = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11))
if mibBuilder.loadTexts: division.setStatus('current')
if mibBuilder.loadTexts: division.setDescription('Distinguish Samsung Company')
oadivision = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5))
if mibBuilder.loadTexts: oadivision.setStatus('current')
if mibBuilder.loadTexts: oadivision.setDescription('Distinguish Samsung Electronics Division')
samsungCommonMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11))
if mibBuilder.loadTexts: samsungCommonMIB.setStatus('current')
if mibBuilder.loadTexts: samsungCommonMIB.setDescription('Samsung Common MIB')
mibBuilder.exportSymbols("SAMSUNG-COMMON-MIB", oadivision=oadivision, PYSNMP_MODULE_ID=samsung, samsung=samsung, division=division, samsungCommonMIB=samsungCommonMIB)
