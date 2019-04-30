#
# PySNMP MIB module CISCO-IETF-ISIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-ISIS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, Gauge32, Counter64, TimeTicks, Counter32, MibIdentifier, Integer32, iso, ObjectIdentity, NotificationType, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Counter64", "TimeTicks", "Counter32", "MibIdentifier", "Integer32", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfIsisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 446))
ciscoIetfIsisCapability.setRevisions(('2005-08-18 00:00',))
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setLastUpdated('200508180000Z')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfIsisCapV12R0225SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 446, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setProductRelease('Cisco IOS 12.2(25)SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-ISIS-CAPABILITY", ciscoIetfIsisCapability=ciscoIetfIsisCapability, ciscoIetfIsisCapV12R0225SG=ciscoIetfIsisCapV12R0225SG, PYSNMP_MODULE_ID=ciscoIetfIsisCapability)
