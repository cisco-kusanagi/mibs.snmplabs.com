#
# PySNMP MIB module CISCO-WAN-VISM-CAS-GRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-CAS-GRP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, TimeTicks, Unsigned32, Bits, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Unsigned32", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismCasGrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 333))
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setLastUpdated('200012050000Z')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setOrganization('Cisco Systems, Inc.')
cwvismCasGrpCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setProductRelease('VISM Release 2.1.0 and MGX-8850 Release 1.1.34')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-CAS-GRP-CAPABILITY", ciscoWanVismCasGrpCapability=ciscoWanVismCasGrpCapability, cwvismCasGrpCapability1=cwvismCasGrpCapability1, PYSNMP_MODULE_ID=ciscoWanVismCasGrpCapability)
