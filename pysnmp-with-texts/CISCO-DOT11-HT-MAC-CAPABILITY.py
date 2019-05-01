#
# PySNMP MIB module CISCO-DOT11-HT-MAC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-MAC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, IpAddress, iso, Gauge32, NotificationType, Unsigned32, Bits, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "Gauge32", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "MibIdentifier", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cDot11HtMacCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 550))
cDot11HtMacCapability.setRevisions(('2007-07-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cDot11HtMacCapability.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: cDot11HtMacCapability.setLastUpdated('200707260000Z')
if mibBuilder.loadTexts: cDot11HtMacCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11HtMacCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: cDot11HtMacCapability.setDescription('Agent capabilities for CISCO-DOT11-HT-MAC-MIB')
cDot11HtMacCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 550, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setStatus('current')
if mibBuilder.loadTexts: cDot11HtMacCapabilityV12R0410BJA.setDescription('Cisco DOT11 HT MAC MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-HT-MAC-CAPABILITY", cDot11HtMacCapabilityV12R0410BJA=cDot11HtMacCapabilityV12R0410BJA, cDot11HtMacCapability=cDot11HtMacCapability, PYSNMP_MODULE_ID=cDot11HtMacCapability)
