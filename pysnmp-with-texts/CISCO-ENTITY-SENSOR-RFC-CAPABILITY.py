#
# PySNMP MIB module CISCO-ENTITY-SENSOR-RFC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-SENSOR-RFC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Counter32, iso, Bits, Integer32, Unsigned32, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter32", "iso", "Bits", "Integer32", "Unsigned32", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEntitySensorRfcCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 430))
ciscoEntitySensorRfcCapability.setRevisions(('2008-02-08 00:00', '2006-05-31 00:00', '2005-01-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setRevisionsDescriptions(('Added cEntSensorRfcCapc4710aceVA1R70 agent capabilities for ACE 4710 Application Control Engine Appliance.', 'Added cEntSensorRfcCapACSWV03R000 for Application Control Engine(ACE) Service Module.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setLastUpdated('200802080000Z')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntitySensorRfcCapability.setDescription('The capabilities description of ENTITY-SENSOR-MIB.')
cEntSensorRfcCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapCatOSV08R0501 = cEntSensorRfcCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapCatOSV08R0501.setDescription('ENTITY-SENSOR-MIB capabilities.')
cEntSensorRfcCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) \n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapACSWV03R000 = cEntSensorRfcCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapACSWV03R000.setDescription('ENTITY-SENSOR-MIB capabilities.')
cEntSensorRfcCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 430, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntSensorRfcCapc4710aceVA1R70 = cEntSensorRfcCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: cEntSensorRfcCapc4710aceVA1R70.setDescription('ENTITY-SENSOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-SENSOR-RFC-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntitySensorRfcCapability, ciscoEntitySensorRfcCapability=ciscoEntitySensorRfcCapability, cEntSensorRfcCapACSWV03R000=cEntSensorRfcCapACSWV03R000, cEntSensorRfcCapc4710aceVA1R70=cEntSensorRfcCapc4710aceVA1R70, cEntSensorRfcCapCatOSV08R0501=cEntSensorRfcCapCatOSV08R0501)
