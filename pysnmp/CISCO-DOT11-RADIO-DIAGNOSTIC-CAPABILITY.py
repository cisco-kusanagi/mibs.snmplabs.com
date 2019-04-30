#
# PySNMP MIB module CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, MibIdentifier, TimeTicks, ModuleIdentity, Counter64, Bits, NotificationType, IpAddress, Counter32, Integer32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter64", "Bits", "NotificationType", "IpAddress", "Counter32", "Integer32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDot11RadioDiagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 335))
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setLastUpdated('200309030000Z')
if mibBuilder.loadTexts: ciscoDot11RadioDiagCapability.setOrganization('Cisco Systems, Inc.')
ciscoDot11RadioDiagCapabilityV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11RadioDiagCapabilityV1 = ciscoDot11RadioDiagCapabilityV1.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-RADIO-DIAGNOSTIC-CAPABILITY", ciscoDot11RadioDiagCapabilityV1=ciscoDot11RadioDiagCapabilityV1, PYSNMP_MODULE_ID=ciscoDot11RadioDiagCapability, ciscoDot11RadioDiagCapability=ciscoDot11RadioDiagCapability)
