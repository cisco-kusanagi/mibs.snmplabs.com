#
# PySNMP MIB module CISCO-NAC-NAD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NAC-NAD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:08:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, NotificationType, ObjectIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, Gauge32, Counter64, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "NotificationType", "ObjectIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoNacNadCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 440))
ciscoNacNadCapability.setRevisions(('2008-11-10 00:00', '2008-07-17 00:00', '2006-12-12 00:00', '2005-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNacNadCapability.setRevisionsDescriptions(('Updated capabilities statement CISCO-NAC-NAD-MIB for 3750.', 'Added capability statement ciscoNacNadCapCatOSV08R0701.', 'Added capability statement ciscoNacNadCapCatOSV08R0601.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNacNadCapability.setLastUpdated('200811100000Z')
if mibBuilder.loadTexts: ciscoNacNadCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNacNadCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-nac@cisco.com, cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNacNadCapability.setDescription('The capabilities description of CISCO-NAC-NAD-MIB.')
ciscoNacNadCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0501 = ciscoNacNadCapCatOSV08R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0501.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0601 = ciscoNacNadCapCatOSV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0601.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapCatOSV08R0701 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setProductRelease('Cisco CatOS 8.7(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapCatOSV08R0701 = ciscoNacNadCapCatOSV08R0701.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapCatOSV08R0701.setDescription('CISCO-NAC-NAD-MIB capabilities.')
ciscoNacNadCapV12R0246SECat3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 440, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setProductRelease('Cisco IOS 12.2(46)SE on Catalyst 3750.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNacNadCapV12R0246SECat3k = ciscoNacNadCapV12R0246SECat3k.setStatus('current')
if mibBuilder.loadTexts: ciscoNacNadCapV12R0246SECat3k.setDescription('CISCO-NAC-NAD-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-NAC-NAD-CAPABILITY", ciscoNacNadCapability=ciscoNacNadCapability, ciscoNacNadCapCatOSV08R0701=ciscoNacNadCapCatOSV08R0701, ciscoNacNadCapCatOSV08R0601=ciscoNacNadCapCatOSV08R0601, ciscoNacNadCapCatOSV08R0501=ciscoNacNadCapCatOSV08R0501, ciscoNacNadCapV12R0246SECat3k=ciscoNacNadCapV12R0246SECat3k, PYSNMP_MODULE_ID=ciscoNacNadCapability)
