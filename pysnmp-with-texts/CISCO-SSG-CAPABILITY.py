#
# PySNMP MIB module CISCO-SSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SSG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, ObjectIdentity, Counter32, TimeTicks, MibIdentifier, Gauge32, iso, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "ObjectIdentity", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "iso", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 1500))
ciscoSsgCapability.setRevisions(('2004-08-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSsgCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSsgCapability.setLastUpdated('200408130000Z')
if mibBuilder.loadTexts: ciscoSsgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSsgCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ssg@cisco.com')
if mibBuilder.loadTexts: ciscoSsgCapability.setDescription('This is the Agent Capability MIB for CISCO-SSG-MIB.')
ciscoSsgCapabilityV12R03RevT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 1500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setStatus('current')
if mibBuilder.loadTexts: ciscoSsgCapabilityV12R03RevT.setDescription('CISCO-SSG-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SSG-CAPABILITY", ciscoSsgCapability=ciscoSsgCapability, PYSNMP_MODULE_ID=ciscoSsgCapability, ciscoSsgCapabilityV12R03RevT=ciscoSsgCapabilityV12R03RevT)
