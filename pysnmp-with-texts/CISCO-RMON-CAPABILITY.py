#
# PySNMP MIB module CISCO-RMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RMON-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, Counter64, Counter32, Bits, TimeTicks, NotificationType, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, IpAddress, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Counter32", "Bits", "TimeTicks", "NotificationType", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "IpAddress", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 357))
ciscoRmonCapability.setRevisions(('2008-08-04 00:00', '2006-03-09 00:00', '2004-04-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRmonCapability.setRevisionsDescriptions(('Added capability statement ciscoRmonCapNXOSV04R0101PMDS9000.', 'Add VARIATIONs for notifications fallingAlarm and risingAlarm in ciscoRmonCapCatOSV08R0101.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRmonCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoRmonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRmonCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-rmon@cisco.com')
if mibBuilder.loadTexts: ciscoRmonCapability.setDescription('The capabilities description of RMON-MIB.')
ciscoRmonCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapCatOSV08R0101 = ciscoRmonCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonCapCatOSV08R0101.setDescription('RMON-MIB capabilities.')
ciscoRmonCapNXOSV04R0101PMDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 357, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setProductRelease('Cisco NX-OS 4.1(1) on MDS9000 Storage Switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRmonCapNXOSV04R0101PMDS9000 = ciscoRmonCapNXOSV04R0101PMDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoRmonCapNXOSV04R0101PMDS9000.setDescription('RMON-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RMON-CAPABILITY", ciscoRmonCapCatOSV08R0101=ciscoRmonCapCatOSV08R0101, ciscoRmonCapNXOSV04R0101PMDS9000=ciscoRmonCapNXOSV04R0101PMDS9000, ciscoRmonCapability=ciscoRmonCapability, PYSNMP_MODULE_ID=ciscoRmonCapability)
