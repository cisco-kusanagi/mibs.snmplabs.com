#
# PySNMP MIB module TRAPEZE-NETWORKS-QOS-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-QOS-CONFIG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, NotificationType, iso, Gauge32, Counter64, ModuleIdentity, Counter32, Unsigned32, Integer32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "NotificationType", "iso", "Gauge32", "Counter64", "ModuleIdentity", "Counter32", "Unsigned32", "Integer32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzQosConfigMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 20))
trpzQosConfigMib.setRevisions(('2011-02-24 00:11',))
if mibBuilder.loadTexts: trpzQosConfigMib.setLastUpdated('201102240011Z')
if mibBuilder.loadTexts: trpzQosConfigMib.setOrganization('Trapeze Networks')
trpzQosConfigMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1))
trpzQosConfQosProfileConfigTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1), )
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigTable.setStatus('current')
trpzQosConfQosProfileConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfProfileName"))
if mibBuilder.loadTexts: trpzQosConfQosProfileConfigEntry.setStatus('current')
trpzQosConfQosProfConfProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: trpzQosConfQosProfConfProfileName.setStatus('current')
trpzQosConfQosProfConfMaxBandwidthKbps = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 20, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trpzQosConfQosProfConfMaxBandwidthKbps.setStatus('current')
trpzQosConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2))
trpzQosConfigCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1))
trpzQosConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2))
trpzQosConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfileConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfigCompliance = trpzQosConfigCompliance.setStatus('current')
trpzQosConfQosProfileConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 20, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", "trpzQosConfQosProfConfMaxBandwidthKbps"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzQosConfQosProfileConfigGroup = trpzQosConfQosProfileConfigGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-QOS-CONFIG-MIB", trpzQosConfQosProfileConfigTable=trpzQosConfQosProfileConfigTable, trpzQosConfQosProfileConfigEntry=trpzQosConfQosProfileConfigEntry, trpzQosConfigMibObjects=trpzQosConfigMibObjects, trpzQosConfigConformance=trpzQosConfigConformance, PYSNMP_MODULE_ID=trpzQosConfigMib, trpzQosConfigCompliances=trpzQosConfigCompliances, trpzQosConfigGroups=trpzQosConfigGroups, trpzQosConfigCompliance=trpzQosConfigCompliance, trpzQosConfQosProfConfMaxBandwidthKbps=trpzQosConfQosProfConfMaxBandwidthKbps, trpzQosConfQosProfileConfigGroup=trpzQosConfQosProfileConfigGroup, trpzQosConfigMib=trpzQosConfigMib, trpzQosConfQosProfConfProfileName=trpzQosConfQosProfConfProfileName)
