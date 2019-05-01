#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:55:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Integer32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Unsigned32, IpAddress, Counter64, Bits, TimeTicks, Gauge32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter64", "Bits", "TimeTicks", "Gauge32", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDot11RadioDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 335))
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setLastUpdated('200309030000Z')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setDescription('Agent capabilities for CISCO-DOT11-RADIO-DIAGNOSTIC-MIB')
ciscoDot11RadioDiagCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapabilityV1.setDescription('Cisco Dot11 RADIO DIAGNOSTIC MIB capabilities')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY", PYSNMP_MODULE_ID=ciscoDot11RadioDiagCapability, ciscoDot11RadioDiagCapabilityV1=ciscoDot11RadioDiagCapabilityV1, ciscoDot11RadioDiagCapability=ciscoDot11RadioDiagCapability)
