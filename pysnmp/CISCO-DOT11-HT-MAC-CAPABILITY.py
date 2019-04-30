#
# PySNMP MIB module CISCO-DOT11-HT-MAC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-MAC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, IpAddress, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, Counter64, Gauge32, Bits, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "IpAddress", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter64", "Gauge32", "Bits", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
cDot11HtMacCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 550))
cDot11HtMacCapability.setRevisions(('2007-07-26 00:00',))
if mibBuilder.loadTexts: cDot11HtMacCapability.setLastUpdated('200707260000Z')
if mibBuilder.loadTexts: cDot11HtMacCapability.setOrganization('Cisco Systems, Inc.')
cDot11HtMacCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 550, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtMacCapabilityV12R0410BJA = cDot11HtMacCapabilityV12R0410BJA.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-HT-MAC-CAPABILITY", PYSNMP_MODULE_ID=cDot11HtMacCapability, cDot11HtMacCapabilityV12R0410BJA=cDot11HtMacCapabilityV12R0410BJA, cDot11HtMacCapability=cDot11HtMacCapability)
