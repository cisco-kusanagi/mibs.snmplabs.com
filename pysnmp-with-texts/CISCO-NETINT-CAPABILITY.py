#
# PySNMP MIB module CISCO-NETINT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NETINT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:08:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter32, Integer32, IpAddress, Counter64, ModuleIdentity, Bits, MibIdentifier, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32", "IpAddress", "Counter64", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetintCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 452))
ciscoNetintCapability.setRevisions(('2007-07-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNetintCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNetintCapability.setLastUpdated('200707030000Z')
if mibBuilder.loadTexts: ciscoNetintCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNetintCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNetintCapability.setDescription('The capabilities description of CISCO-NETINT-MIB.')
ciscoNetintCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 452, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintCapV12R0233SXHPCat6k = ciscoNetintCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: ciscoNetintCapV12R0233SXHPCat6k.setDescription('CISCO-NETINT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-NETINT-CAPABILITY", ciscoNetintCapV12R0233SXHPCat6k=ciscoNetintCapV12R0233SXHPCat6k, ciscoNetintCapability=ciscoNetintCapability, PYSNMP_MODULE_ID=ciscoNetintCapability)
