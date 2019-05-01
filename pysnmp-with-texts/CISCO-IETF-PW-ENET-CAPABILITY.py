#
# PySNMP MIB module CISCO-IETF-PW-ENET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-ENET-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, TimeTicks, NotificationType, Gauge32, IpAddress, ObjectIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "TimeTicks", "NotificationType", "Gauge32", "IpAddress", "ObjectIdentity", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPwEnetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 428))
ciscoIetfPwEnetCapability.setRevisions(('2004-11-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setRevisionsDescriptions(('Initial version: ciscoIetfPwEnetCapabilityV12R00 ',))
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setLastUpdated('200411291200Z')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: mpls-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setDescription('Agent capabilities for CISCO-IETF-PW-ENET-MIB')
ciscoIetfPwEnetCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 428, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapabilityV12R00.setDescription('Pseudowire Ethernet MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-PW-ENET-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapabilityV12R00=ciscoIetfPwEnetCapabilityV12R00, ciscoIetfPwEnetCapability=ciscoIetfPwEnetCapability)
