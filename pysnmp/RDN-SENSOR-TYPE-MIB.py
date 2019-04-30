#
# PySNMP MIB module RDN-SENSOR-TYPE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RDN-SENSOR-TYPE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rdnDefinitions, = mibBuilder.importSymbols("RDN-DEFINITIONS-MIB", "rdnDefinitions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, NotificationType, ModuleIdentity, Gauge32, Unsigned32, TimeTicks, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, MibIdentifier, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "NotificationType", "ModuleIdentity", "Gauge32", "Unsigned32", "TimeTicks", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "MibIdentifier", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSensorTypes = ModuleIdentity((1, 3, 6, 1, 4, 1, 4981, 4, 6))
rdnSensorTypes.setRevisions(('2008-08-08 00:00', '2003-11-05 00:00', '2001-08-07 00:00',))
if mibBuilder.loadTexts: rdnSensorTypes.setLastUpdated('200808080000Z')
if mibBuilder.loadTexts: rdnSensorTypes.setOrganization('Motorola')
rdnSensorsUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 0))
rdnSensorsSRM750 = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 1))
rdnSensorsSRMDIMM = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 2))
rdnSensorsSRMDC2DC = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 3))
rdnSensorsSRMXFAB = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 4))
rdnSensorsFan = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 4, 6, 5))
mibBuilder.exportSymbols("RDN-SENSOR-TYPE-MIB", rdnSensorsUnknown=rdnSensorsUnknown, rdnSensorsSRMDIMM=rdnSensorsSRMDIMM, rdnSensorsSRMDC2DC=rdnSensorsSRMDC2DC, PYSNMP_MODULE_ID=rdnSensorTypes, rdnSensorsSRMXFAB=rdnSensorsSRMXFAB, rdnSensorsFan=rdnSensorsFan, rdnSensorTypes=rdnSensorTypes, rdnSensorsSRM750=rdnSensorsSRM750)
