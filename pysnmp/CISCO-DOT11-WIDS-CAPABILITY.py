#
# PySNMP MIB module CISCO-DOT11-WIDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-WIDS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Gauge32, Counter32, iso, MibIdentifier, IpAddress, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "iso", "MibIdentifier", "IpAddress", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDot11WidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 426))
if mibBuilder.loadTexts: cDot11WidsCapability.setLastUpdated('200501240000Z')
if mibBuilder.loadTexts: cDot11WidsCapability.setOrganization('Cisco Systems, Inc.')
cDot11WidsCapabilityV12R0304JA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 426, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-WIDS-CAPABILITY", cDot11WidsCapabilityV12R0304JA=cDot11WidsCapabilityV12R0304JA, PYSNMP_MODULE_ID=cDot11WidsCapability, cDot11WidsCapability=cDot11WidsCapability)
