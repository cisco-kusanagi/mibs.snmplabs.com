#
# PySNMP MIB module CISCO-HC-ALARM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-HC-ALARM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, iso, Gauge32, TimeTicks, Integer32, Unsigned32, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "TimeTicks", "Integer32", "Unsigned32", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity")
DisplayString, StorageType, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention")
ciscoHcAlarmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 398))
ciscoHcAlarmCapability.setRevisions(('2008-08-05 00:00', '2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoHcAlarmCapability.setRevisionsDescriptions(('Added capability statement ciscoHcAlarmCapNXOSV04R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setLastUpdated('200808050000Z')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoHcAlarmCapability.setDescription('The capabilities description of HC-ALARM-MIB.')
ciscoHcAlarmCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapCatOSV08R0401 = ciscoHcAlarmCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapCatOSV08R0401.setDescription('HC-ALARM-MIB capabilities.')
ciscoHcAlarmCapNXOSV04R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 398, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoHcAlarmCapNXOSV04R0101 = ciscoHcAlarmCapNXOSV04R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoHcAlarmCapNXOSV04R0101.setDescription('HC-RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-HC-ALARM-CAPABILITY", ciscoHcAlarmCapCatOSV08R0401=ciscoHcAlarmCapCatOSV08R0401, PYSNMP_MODULE_ID=ciscoHcAlarmCapability, ciscoHcAlarmCapability=ciscoHcAlarmCapability, ciscoHcAlarmCapNXOSV04R0101=ciscoHcAlarmCapNXOSV04R0101)
