#
# PySNMP MIB module CISCO-VISM-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VISM-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:18:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
IpAddress, MibIdentifier, TimeTicks, Unsigned32, Gauge32, Counter64, ModuleIdentity, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "TimeTicks", "Unsigned32", "Gauge32", "Counter64", "ModuleIdentity", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVismModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 458))
ciscoVismModuleCapability.setRevisions(('2005-10-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismModuleCapability.setRevisionsDescriptions(('Initial version of this capability file.',))
if mibBuilder.loadTexts: ciscoVismModuleCapability.setLastUpdated('200510180000Z')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoVismModuleCapability.setDescription('The capabilities description of CISCO-VISM-MODULE-MIB.')
cVismModuleCapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 458, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismModuleCapabilityV3325 = cVismModuleCapabilityV3325.setStatus('current')
if mibBuilder.loadTexts: cVismModuleCapabilityV3325.setDescription('CISCO-VISM-MODULE-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-MODULE-CAPABILITY", ciscoVismModuleCapability=ciscoVismModuleCapability, cVismModuleCapabilityV3325=cVismModuleCapabilityV3325, PYSNMP_MODULE_ID=ciscoVismModuleCapability)
