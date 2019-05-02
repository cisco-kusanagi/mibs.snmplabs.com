#
# PySNMP MIB module CISCO-ITP-MLR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-MLR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, Integer32, Bits, Counter64, iso, MibIdentifier, Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Integer32", "Bits", "Counter64", "iso", "MibIdentifier", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMlrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 423))
ciscoMlrCapability.setRevisions(('2007-05-18 00:00', '2006-10-05 00:00', '2005-02-18 00:00', '2004-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMlrCapability.setRevisionsDescriptions(('Added ciscoMlrCapabilityV12R0411SW capabilities statement.', 'Added ciscoMlrCapabilityV12R0218IXA capabilities statement.', 'Added ciscoMlrCapabilityV12R0225SW01 capability statement. Replace the ciscoMlrRuleSetGroup group with ciscoMlrRuleSetGroupRev2 to support additional rule parameters.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMlrCapability.setLastUpdated('200705180000Z')
if mibBuilder.loadTexts: ciscoMlrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMlrCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoMlrCapability.setDescription('Agent capabilities for the CISCO-ITP-MLR-MIB.')
ciscoMlrCapabilityV12R0221SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setProductRelease('Cisco IOS 12.2(21)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0221SW01 = ciscoMlrCapabilityV12R0221SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0221SW01.setDescription('IOS 12.2(21)SW1 Cisco CISCO-ITP-MLR-MIB.my User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0225SW01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0225SW01 = ciscoMlrCapabilityV12R0225SW01.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0225SW01.setDescription('IOS 12.2(25)SW1 Cisco CISCO-ITP-MLR-MIB.my User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0218IXA = ciscoMlrCapabilityV12R0218IXA.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0218IXA.setDescription('IOS 12.2(18)IXA Cisco CISCO-ITP-MLR-MIB.my User Agent MIB capabilities.')
ciscoMlrCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 423, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMlrCapabilityV12R0411SW = ciscoMlrCapabilityV12R0411SW.setStatus('current')
if mibBuilder.loadTexts: ciscoMlrCapabilityV12R0411SW.setDescription('Cisco IOS 12.4(11)SW CISCO-ITP-MLR-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MLR-CAPABILITY", ciscoMlrCapabilityV12R0221SW01=ciscoMlrCapabilityV12R0221SW01, ciscoMlrCapabilityV12R0225SW01=ciscoMlrCapabilityV12R0225SW01, ciscoMlrCapability=ciscoMlrCapability, PYSNMP_MODULE_ID=ciscoMlrCapability, ciscoMlrCapabilityV12R0411SW=ciscoMlrCapabilityV12R0411SW, ciscoMlrCapabilityV12R0218IXA=ciscoMlrCapabilityV12R0218IXA)
