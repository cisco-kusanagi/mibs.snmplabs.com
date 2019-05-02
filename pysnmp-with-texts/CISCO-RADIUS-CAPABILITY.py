#
# PySNMP MIB module CISCO-RADIUS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Counter64, NotificationType, TimeTicks, MibIdentifier, Unsigned32, Counter32, ModuleIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "NotificationType", "TimeTicks", "MibIdentifier", "Unsigned32", "Counter32", "ModuleIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRadiusCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 399))
ciscoRadiusCapability.setRevisions(('2008-05-21 00:00', '2007-01-17 00:00', '2004-06-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusCapability.setRevisionsDescriptions(('Added capability statement ciscoRadiusCapCatOSV08R0701.', 'Added capability statement ciscoRadiusCapCatOSV08R0601. Removed the VARIATION crRadiusServerType from ciscoRadiusCapCatOSV08R0401.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRadiusCapability.setLastUpdated('200805210000Z')
if mibBuilder.loadTexts: ciscoRadiusCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusCapability.setDescription('The capabilities description of CISCO-RADIUS-MIB.')
ciscoRadiusCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0401 = ciscoRadiusCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0401 = ciscoRadiusCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0401.setDescription('CISCO-RADIUS-MIB capabilities.')
ciscoRadiusCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0601 = ciscoRadiusCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0601 = ciscoRadiusCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0601.setDescription('CISCO-RADIUS-MIB capabilities.')
ciscoRadiusCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 399, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0701 = ciscoRadiusCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusCapCatOSV08R0701 = ciscoRadiusCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusCapCatOSV08R0701.setDescription('CISCO-RADIUS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RADIUS-CAPABILITY", ciscoRadiusCapCatOSV08R0401=ciscoRadiusCapCatOSV08R0401, ciscoRadiusCapability=ciscoRadiusCapability, ciscoRadiusCapCatOSV08R0701=ciscoRadiusCapCatOSV08R0701, PYSNMP_MODULE_ID=ciscoRadiusCapability, ciscoRadiusCapCatOSV08R0601=ciscoRadiusCapCatOSV08R0601)
