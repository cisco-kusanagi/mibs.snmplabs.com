#
# PySNMP MIB module CISCO-MODULE-VIRTUALIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MODULE-VIRTUALIZATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ObjectIdentity, NotificationType, IpAddress, TimeTicks, Gauge32, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Integer32, iso, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Integer32", "iso", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoModuleVirtualizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 497))
ciscoModuleVirtualizationCapability.setRevisions(('2008-06-14 00:00', '2006-05-31 00:00', '2006-03-21 00:00',))
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setLastUpdated('200806140000Z')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setOrganization('Cisco Systems, Inc.')
ciscoModuleVirtualizationCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setStatus('current')
ciscoModVirtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-VIRTUALIZATION-CAPABILITY", ciscoModuleVirtualizationCapabilityACSWV03R000=ciscoModuleVirtualizationCapabilityACSWV03R000, PYSNMP_MODULE_ID=ciscoModuleVirtualizationCapability, ciscoModuleVirtualizationCapability=ciscoModuleVirtualizationCapability, ciscoModVirtCapc4710aceVA1R700=ciscoModVirtCapc4710aceVA1R700)
