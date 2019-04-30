#
# PySNMP MIB module CISCO-DOT11-HT-PHY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-PHY-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter32, Unsigned32, MibIdentifier, Integer32, IpAddress, Counter64, Bits, NotificationType, ModuleIdentity, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter32", "Unsigned32", "MibIdentifier", "Integer32", "IpAddress", "Counter64", "Bits", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
cDot11HtPhyCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 551))
cDot11HtPhyCapability.setRevisions(('2007-08-22 00:00',))
if mibBuilder.loadTexts: cDot11HtPhyCapability.setLastUpdated('200708220000Z')
if mibBuilder.loadTexts: cDot11HtPhyCapability.setOrganization('Cisco Systems, Inc.')
cDot11HtPhyCapabilityV12R0410BJA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 551, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setProductRelease('Cisco IOS 12.4(10b)JA for the AP1250 802.11 \n                         Access Points')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11HtPhyCapabilityV12R0410BJA = cDot11HtPhyCapabilityV12R0410BJA.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-HT-PHY-CAPABILITY", cDot11HtPhyCapabilityV12R0410BJA=cDot11HtPhyCapabilityV12R0410BJA, PYSNMP_MODULE_ID=cDot11HtPhyCapability, cDot11HtPhyCapability=cDot11HtPhyCapability)
