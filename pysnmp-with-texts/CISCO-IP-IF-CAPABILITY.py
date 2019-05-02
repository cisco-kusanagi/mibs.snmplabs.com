#
# PySNMP MIB module CISCO-IP-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IP-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, Gauge32, iso, ObjectIdentity, Unsigned32, IpAddress, NotificationType, ModuleIdentity, Integer32, MibIdentifier, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "iso", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "ModuleIdentity", "Integer32", "MibIdentifier", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIPIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 324))
ciscoIPIfCapability.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIPIfCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIPIfCapability.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: ciscoIPIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIPIfCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIPIfCapability.setDescription('The capabilities description of CISCO-IP-IF-MIB.')
ciscoIpIfCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 324, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpIfCapCatOSV08R0101 = ciscoIpIfCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpIfCapCatOSV08R0101 = ciscoIpIfCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoIpIfCapCatOSV08R0101.setDescription('CISCO-IP-IF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-IF-CAPABILITY", ciscoIPIfCapability=ciscoIPIfCapability, ciscoIpIfCapCatOSV08R0101=ciscoIpIfCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoIPIfCapability)
