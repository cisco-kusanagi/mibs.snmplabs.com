#
# PySNMP MIB module CISCO-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NETFLOW-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:08:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NfTopFlowsSortTypes, = mibBuilder.importSymbols("CISCO-NETFLOW-MIB", "NfTopFlowsSortTypes")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Gauge32, iso, Counter32, Counter64, IpAddress, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Gauge32", "iso", "Counter32", "Counter64", "IpAddress", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 407))
ciscoNetflowCapability.setRevisions(('2010-11-04 00:01', '2007-08-24 00:00', '2004-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNetflowCapability.setRevisionsDescriptions(('Added capability statement ciscoNetflowCapV12R0250SYPCat6kPfc4.', 'Added ciscoNetflowCapV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNetflowCapability.setLastUpdated('201011040001Z')
if mibBuilder.loadTexts: ciscoNetflowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNetflowCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-netflow-mib@cisco.com')
if mibBuilder.loadTexts: ciscoNetflowCapability.setDescription('The capabilities description of CISCO-NETFLOW-MIB.')
ciscoNetflowCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapCatOSV08R0401.setDescription('CISCO-NETFLOW-MIB capabilities.')
ciscoNetflowCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapV12R0233SXHPCat6K.setDescription('CISCO-NETFLOW-MIB capabilities.')
ciscoNetflowCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapV12R0250SYPCat6kPfc4.setDescription('CISCO-NETFLOW-MIB is not supported.')
mibBuilder.exportSymbols("CISCO-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoNetflowCapability, ciscoNetflowCapCatOSV08R0401=ciscoNetflowCapCatOSV08R0401, ciscoNetflowCapability=ciscoNetflowCapability, ciscoNetflowCapV12R0233SXHPCat6K=ciscoNetflowCapV12R0233SXHPCat6K, ciscoNetflowCapV12R0250SYPCat6kPfc4=ciscoNetflowCapV12R0250SYPCat6kPfc4)
