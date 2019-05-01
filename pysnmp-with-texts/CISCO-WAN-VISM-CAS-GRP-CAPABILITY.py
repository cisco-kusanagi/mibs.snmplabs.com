#
# PySNMP MIB module CISCO-WAN-VISM-CAS-GRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-VISM-CAS-GRP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:21:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, iso, Gauge32, MibIdentifier, Counter64, NotificationType, Integer32, Unsigned32, TimeTicks, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "Integer32", "Unsigned32", "TimeTicks", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanVismCasGrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 333))
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setLastUpdated('200012050000Z')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanVismCasGrpCapability.setDescription('The Agent Capabilities for vismCasGrp.my .')
cwvismCasGrpCapability1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setProductRelease('VISM Release 2.1.0 and MGX-8850 Release 1.1.34')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwvismCasGrpCapability1 = cwvismCasGrpCapability1.setStatus('current')
if mibBuilder.loadTexts: cwvismCasGrpCapability1.setDescription('vismCasGrp.my Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-CAS-GRP-CAPABILITY", ciscoWanVismCasGrpCapability=ciscoWanVismCasGrpCapability, cwvismCasGrpCapability1=cwvismCasGrpCapability1, PYSNMP_MODULE_ID=ciscoWanVismCasGrpCapability)
