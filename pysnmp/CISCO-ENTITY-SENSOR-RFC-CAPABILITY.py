#
# PySNMP MIB module CISCO-ENTITY-SENSOR-RFC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, Bits, IpAddress, ModuleIdentity, Integer32, Gauge32, TimeTicks, ObjectIdentity, Counter64, Unsigned32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "Gauge32", "TimeTicks", "ObjectIdentity", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntitySensorRfcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 430))
ciscoEntitySensorRfcCapability.setRevisions(('2008-02-08 00:00', '2006-05-31 00:00', '2005-01-31 00:00',))
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setLastUpdated('200802080000Z')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setOrganization('Cisco Systems, Inc.')
cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setStatus('current')
cEntSensorRfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setStatus('current')
cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-RFC-CAPABILITY", ciscoEntitySensorRfcCapability=ciscoEntitySensorRfcCapability, cEntSensorRfcCapACSWV03R000=cEntSensorRfcCapACSWV03R000, cEntSensorRfcCapc4710aceVA1R70=cEntSensorRfcCapc4710aceVA1R70, cEntSensorRfcCapCatOSV08R0501=cEntSensorRfcCapCatOSV08R0501, PYSNMP_MODULE_ID=ciscoEntitySensorRfcCapability)
