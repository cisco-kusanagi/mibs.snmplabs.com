#
# PySNMP MIB module CISCO-POP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-POP-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:09:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ModuleIdentity, iso, Unsigned32, Counter32, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ModuleIdentity", "iso", "Unsigned32", "Counter32", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPopMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 447))
ciscoPopMgmtCapability.setRevisions(('2005-10-12 00:00', '2005-08-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPopMgmtCapability.setRevisionsDescriptions(('Added variations for cpmDS0UsageGroupRev2.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setLastUpdated('200510120000Z')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoPopMgmtCapability.setDescription('Agent capabilities for CISCO-POP-MGMT-MIB.')
ciscoPopMgmtCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 447, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setProductRelease('Cisco IOS 12.4 for C3600 family platforms')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPopMgmtCapabilityV12R04 = ciscoPopMgmtCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoPopMgmtCapabilityV12R04.setDescription('Cisco POP management agent capabilities for C3600 family platforms')
mibBuilder.exportSymbols("CISCO-POP-MGMT-CAPABILITY", ciscoPopMgmtCapabilityV12R04=ciscoPopMgmtCapabilityV12R04, ciscoPopMgmtCapability=ciscoPopMgmtCapability, PYSNMP_MODULE_ID=ciscoPopMgmtCapability)
