#
# PySNMP MIB module CISCO-VISM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-CONN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
iso, TimeTicks, ModuleIdentity, Integer32, Gauge32, Counter32, Counter64, ObjectIdentity, Bits, NotificationType, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "Bits", "NotificationType", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 400))
ciscoVismConnCapability.setRevisions(('2004-03-17 00:00',))
if mibBuilder.loadTexts: ciscoVismConnCapability.setLastUpdated('200403170000Z')
if mibBuilder.loadTexts: ciscoVismConnCapability.setOrganization('Cisco Systems, Inc.')
cVismConnCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 400, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismConnCapabilityV321 = cVismConnCapabilityV321.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-CONN-CAPABILITY", ciscoVismConnCapability=ciscoVismConnCapability, PYSNMP_MODULE_ID=ciscoVismConnCapability, cVismConnCapabilityV321=cVismConnCapabilityV321)
