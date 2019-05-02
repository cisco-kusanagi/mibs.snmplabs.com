#
# PySNMP MIB module CISCO-DOT11-WIDS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-WIDS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Counter64, MibIdentifier, IpAddress, Integer32, ObjectIdentity, Counter32, Unsigned32, Gauge32, TimeTicks, iso, ModuleIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "IpAddress", "Integer32", "ObjectIdentity", "Counter32", "Unsigned32", "Gauge32", "TimeTicks", "iso", "ModuleIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cDot11WidsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 426))
if mibBuilder.loadTexts: cDot11WidsCapability.setLastUpdated('200501240000Z')
if mibBuilder.loadTexts: cDot11WidsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cDot11WidsCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: cDot11WidsCapability.setDescription('Agent capabilities for CISCO-DOT11-WIDS-MIB')
cDot11WidsCapabilityV12R0304JA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 426, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setProductRelease('Cisco IOS 12.3(4) JA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cDot11WidsCapabilityV12R0304JA = cDot11WidsCapabilityV12R0304JA.setStatus('current')
if mibBuilder.loadTexts: cDot11WidsCapabilityV12R0304JA.setDescription('Cisco DOT11 WIDS MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-WIDS-CAPABILITY", cDot11WidsCapabilityV12R0304JA=cDot11WidsCapabilityV12R0304JA, cDot11WidsCapability=cDot11WidsCapability, PYSNMP_MODULE_ID=cDot11WidsCapability)
