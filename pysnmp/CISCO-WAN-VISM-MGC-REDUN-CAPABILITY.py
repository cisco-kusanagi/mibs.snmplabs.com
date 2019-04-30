#
# PySNMP MIB module CISCO-WAN-VISM-MGC-REDUN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-MGC-REDUN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, Counter32, Unsigned32, Gauge32, IpAddress, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, ModuleIdentity, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanVismMgcRedunCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 338))
ciscoWanVismMgcRedunCapability.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setLastUpdated('200108220000Z')
if mibBuilder.loadTexts: ciscoWanVismMgcRedunCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanVismMgcRedunCapV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 338, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setProductRelease('VISM Release2.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanVismMgcRedunCapV2R00 = ciscoWanVismMgcRedunCapV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-MGC-REDUN-CAPABILITY", ciscoWanVismMgcRedunCapV2R00=ciscoWanVismMgcRedunCapV2R00, ciscoWanVismMgcRedunCapability=ciscoWanVismMgcRedunCapability, PYSNMP_MODULE_ID=ciscoWanVismMgcRedunCapability)
