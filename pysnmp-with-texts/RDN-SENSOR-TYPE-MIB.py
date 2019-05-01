#
# PySNMP MIB module RDN-SENSOR-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SENSOR-TYPE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, ObjectIdentity, Unsigned32, Counter32, Bits, Counter64, ModuleIdentity, MibIdentifier, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "ObjectIdentity", "Unsigned32", "Counter32", "Bits", "Counter64", "ModuleIdentity", "MibIdentifier", "IpAddress", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSensorTypes = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 6))
rdnSensorTypes.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2001-08-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rdnSensorTypes.setRevisionsDescriptions(("Added Copyright Statement into MIB modules's description.", 'Updated the CONTACT-INFO.', 'Initial creation.',))
if mibBuilder.loadTexts: rdnSensorTypes.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSensorTypes.setOrganization('Motorola')
if mibBuilder.loadTexts: rdnSensorTypes.setContactInfo('Motorola Customer Service 101 Tournament Drive Horsham, PA 19044 US Tel: +1 888 944 4357 Int Tel: +1 215 323 0044 Fax: +1 215 323 1502 Email: CPSSupport@Motorola.com')
if mibBuilder.loadTexts: rdnSensorTypes.setDescription('MIB module for Motorola Sensor Type definitions. Copyright (C) 2001, 2008 by Motorola, Inc. All rights reserved.')
rdnSensorsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 0))
rdnSensorsSRM750 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 1))
rdnSensorsSRMDIMM = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 2))
rdnSensorsSRMDC2DC = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 3))
rdnSensorsSRMXFAB = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 4))
rdnSensorsFan = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 5))
mibBuilder.exportSymbols("RDN-SENSOR-TYPE-MIB", rdnSensorTypes=rdnSensorTypes, rdnSensorsSRM750=rdnSensorsSRM750, rdnSensorsSRMDC2DC=rdnSensorsSRMDC2DC, rdnSensorsFan=rdnSensorsFan, PYSNMP_MODULE_ID=rdnSensorTypes, rdnSensorsUnknown=rdnSensorsUnknown, rdnSensorsSRMDIMM=rdnSensorsSRMDIMM, rdnSensorsSRMXFAB=rdnSensorsSRMXFAB)
