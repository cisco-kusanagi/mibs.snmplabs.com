#
# PySNMP MIB module CISCO-IETF-PW-ENET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-ENET-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, TimeTicks, iso, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, NotificationType, Gauge32, Unsigned32, Bits, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "iso", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "NotificationType", "Gauge32", "Unsigned32", "Bits", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPwEnetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 428))
ciscoIetfPwEnetCapability.setRevisions(('2004-11-29 12:00',))
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setLastUpdated('200411291200Z')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfPwEnetCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 428, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-ENET-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapability=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapabilityV12R00=ciscoIetfPwEnetCapabilityV12R00)
