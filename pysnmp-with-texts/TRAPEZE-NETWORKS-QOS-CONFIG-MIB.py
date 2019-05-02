#
# PySNMP MIB module TRAPEZE-NETWORKS-QOS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-QOS-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Gauge32, IpAddress, iso, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, ModuleIdentity, MibIdentifier, ObjectIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "IpAddress", "iso", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzQosConfigMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 20))
trpzQosConfigMib.setRevisions(('2011-02-24 00:11',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzQosConfigMib.setRevisionsDescriptions(('v1.0.1: Initial version, for 7.5 release',))
if mibBuilder.loadTexts: trpzQosConfigMib.setLastUpdated('201102240011Z')
if mibBuilder.loadTexts: trpzQosConfigMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzQosConfigMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzQosConfigMib.setDescription("QoS Configuration objects MIB for Trapeze Networks wireless switches. AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB. Copyright (c) 2010-2011 by Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
trpzQosConfigMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1))
trpzQosConfQosProfileConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1), )
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigTable.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigTable.setDescription('A table describing the QoS Profiles configured on this AC.')
trpzQosConfQosProfileConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfProfileName"))
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigEntry.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigEntry.setDescription('Information about a particular QoS Profile on the AC.')
trpzQosConfQosProfConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: trpzQosConfQosProfConfProfileName.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfQosProfConfProfileName.setDescription('The Name of this QoS Profile.')
trpzQosConfQosProfConfMaxBandwidthKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trpzQosConfQosProfConfMaxBandwidthKbps.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfQosProfConfMaxBandwidthKbps.setDescription('The bandwidth limit for an entity using this QoS profile, in Kbits/second. A value of zero means unlimited.')
trpzQosConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2))
trpzQosConfigCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1))
trpzQosConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2))
trpzQosConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfileConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfigCompliance = trpzQosConfigCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfigCompliance.setDescription('The compliance statement for devices that implement QoS Configuration MIB. This compliance statement is for releases 7.5 and greater of AC (wireless switch) software.')
trpzQosConfQosProfileConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfMaxBandwidthKbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfQosProfileConfigGroup = trpzQosConfQosProfileConfigGroup.setStatus('current')
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigGroup.setDescription('Group of columnar objects implemented to provide QoS Profile Configuration info in releases 7.5 and greater.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", trpzQosConfQosProfConfMaxBandwidthKbps=trpzQosConfQosProfConfMaxBandwidthKbps, trpzQosConfigCompliance=trpzQosConfigCompliance, trpzQosConfigMib=trpzQosConfigMib, trpzQosConfQosProfileConfigEntry=trpzQosConfQosProfileConfigEntry, trpzQosConfigGroups=trpzQosConfigGroups, trpzQosConfigMibObjects=trpzQosConfigMibObjects, trpzQosConfigConformance=trpzQosConfigConformance, PYSNMP_MODULE_ID=trpzQosConfigMib, trpzQosConfQosProfileConfigGroup=trpzQosConfQosProfileConfigGroup, trpzQosConfQosProfConfProfileName=trpzQosConfQosProfConfProfileName, trpzQosConfigCompliances=trpzQosConfigCompliances, trpzQosConfQosProfileConfigTable=trpzQosConfQosProfileConfigTable)
