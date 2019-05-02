#
# PySNMP MIB module CISCO-DOT11-HT-PHY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-PHY-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Counter32, Integer32, ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, Counter64, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "Counter64", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cDot11HtPhyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 551))
cDot11HtPhyCapability.setRevisions(('2007-08-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDot11HtPhyCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cDot11HtPhyCapability.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setDescription('Agent capabilities for CISCO-DOT11-HT-PHY-MIB')
cDot11HtPhyCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 551, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setStatus('current')
if mibBuilder.loadTexts: cDot11HtPhyCapabilityV12R0410BJA.setDescription('CISCO-DOT11-HT-PHY-MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-HT-PHY-CAPABILITY", PYSNMP_MODULE_ID=cDot11HtPhyCapability, cDot11HtPhyCapability=cDot11HtPhyCapability, cDot11HtPhyCapabilityV12R0410BJA=cDot11HtPhyCapabilityV12R0410BJA)
