#
# PySNMP MIB module CISCO-VLAN-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VLAN-TRANSLATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, ModuleIdentity, Integer32, TimeTicks, Counter32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Counter64, NotificationType, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Integer32", "TimeTicks", "Counter32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Counter64", "NotificationType", "IpAddress", "Unsigned32")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
ciscoVlanTranslationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 411))
ciscoVlanTranslationMIB.setRevisions(('2004-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setLastUpdated('200406010000Z')
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoVlanTranslationMIB.setDescription('The MIB module for the management of VLAN translations. VLAN translation refers to the ability of the device to translate between different virtual LANs or between VLAN and non-VLAN encapsulating interfaces at Layer 2. Translation is typically used for selective inter-VLAN switching of non-routable protocols and to extend a single VLAN topology across hybrid switching environments.')
ciscoVlanTranslationMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 0))
ciscoVlanTranslationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1))
ciscoVlanTranslationMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2))
cvtGlobalTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1))
cvtGlobalTranslationMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtGlobalTranslationMax.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationMax.setDescription('Maximum number of configurable global VLAN translation entries allowed in the cvtGlobalTranslationTable. A value of zero indicates no limitation on the number of configurable global VLAN translation.')
cvtGlobalTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2), )
if mibBuilder.loadTexts: cvtGlobalTranslationTable.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationTable.setDescription("This table contains the device based VLAN-to-VLAN associations for all the device's physical ports. The translation is applied in both ingress and egress sides of all the Layer 2 trunks. VLAN translation makes the traffic arriving on the VLAN cvtGlobalOriginalVlan on the trunk ports to be mapped to or tagged with the VLAN cvtGlobalTranslatedVlan. It also causes all the traffic internally tagged with the VLAN cvtGlobalTranslatedVlan and leaving the trunk ports to be tagged with VLAN cvtGlobalOriginalVlan. A global VLAN translation configuration is inactive for those ports that are not Layer 2 trunks. The global VLAN translations are mutually exclusive to the port based VLAN translations. The rows in this table can only be created when the table cvtPortTranslationTable is empty. A conceptual row is created for each VLAN mapping configuration on the device which supports the feature. The value of cvtGlobalTranslationMax determines the maximum number of rows in this table.")
cvtGlobalTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalOriginalVlan"))
if mibBuilder.loadTexts: cvtGlobalTranslationEntry.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationEntry.setDescription('Information about the VLAN translation for a particular VLAN to a different VLAN.')
cvtGlobalOriginalVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cvtGlobalOriginalVlan.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalOriginalVlan.setDescription('The VLAN translation is applied in both ingress and egress sides of all the Layer 2 trunks. It makes the traffic arriving on the VLAN with this VLAN ID to be mapped to or tagged with the corresponding instance of cvtGlobalTranslatedVlan on the device. It also causes all the traffic internally tagged with the corresponding instance of cvtGlobalTranslatedVlan and leaving the trunk ports to be tagged with the VLAN of this VLAN ID.')
cvtGlobalTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtGlobalTranslatedVlan.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslatedVlan.setDescription('The VLAN translation is applied in both ingress and egress sides of all the Layer 2 trunks. It makes the traffic arriving on the VLAN with the corresponding instance of cvtGlobalOriginalVlan on the device to be mapped to or tagged with the VLAN of this VLAN ID. It also causes all the traffic internally tagged with the VLAN of this VLAN ID and leaving the trunk ports to be tagged with the corresponding instance of cvtGlobalOriginalVlan on the device.')
cvtGlobalTranslationEffective = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtGlobalTranslationEffective.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationEffective.setDescription('Indicates whether this VLAN translation is functioning on the device.')
cvtGlobalTranslationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtGlobalTranslationStatus.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationStatus.setDescription("The status of the conceptual row for this global VLAN translation. Once a row becomes active, value in any other column within such row cannot be modified. When this object is set to createAndGo(4) and the number of the existing rows exceeds cvtGlobalTranslationMax, agent returns 'resourceUnavailable'.")
cvtPortBasedTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2))
cvtPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1), )
if mibBuilder.loadTexts: cvtPortConfigTable.setStatus('current')
if mibBuilder.loadTexts: cvtPortConfigTable.setDescription('This table contains information related to the port based VLAN translation on the device.')
cvtPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cvtPortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cvtPortConfigEntry.setDescription('A set of configuration information regarding port based VLAN translation. An entry exists for every physical port which supports VLAN translation feature.')
cvtPortTranslationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cvtPortTranslationEnabled.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationEnabled.setDescription("This object indicates whether the VLAN translation feature is enabled on the port. Setting this value to 'true' enables VLAN translation on the port. Setting this value to 'false' disables VLAN translation on the port. The corresponding entries in table cvtPortTranslationTable will not be used if the value of this object is 'false'.")
cvtPortTranslationMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvtPortTranslationMax.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationMax.setDescription('Maximum number of configurable VLAN translation entries allowed on the port. A value of zero indicates no limitation on the number of configurable VLANs which can be translated.')
cvtPortTranslationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2), )
if mibBuilder.loadTexts: cvtPortTranslationTable.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationTable.setDescription("This table contains the port based VLAN-to-VLAN associations for the device's physical ports. The translation is applied in both ingress and egress sides of the layer 2 trunk on the port. It causes the traffic arriving on the VLAN cvtPortOriginalVlan on this port to be mapped to or tagged with the VLAN cvtPortTranslatedVlan. It also causes all the traffic internally tagged with the VLAN cvtPortTranslatedVlan and leaving the port to be tagged with VLAN cvtPortOriginalVlan. A VLAN translation configuration that is applied to Layer 2 ports that are not Layer 2 trunks is inactive. The port based VLAN translations are mutually exclusive to the global VLAN translations. The rows in this table can only be created when the table cvtGlobalTranslationTable is empty. A conceptual row is created for a translation on a particular physical port which supports the feature. The value of the corresponding instance of cvtPortTranslationMax determines the maximum number of rows for the same port. On some platforms, VLAN translation may be configured per port group rather than per port. If multiple ports belong to a port group, the VLAN translation configured to any of the ports in such group will apply to all ports in the same group.")
cvtPortTranslationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-VLAN-TRANSLATION-MIB", "cvtPortOriginalVlan"))
if mibBuilder.loadTexts: cvtPortTranslationEntry.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationEntry.setDescription('Entry containing VLAN translation Information for a particular VLAN on a specific port. The entry is created and deleted by using cvtPortTranslationStatus.')
cvtPortOriginalVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: cvtPortOriginalVlan.setStatus('current')
if mibBuilder.loadTexts: cvtPortOriginalVlan.setDescription('The VLAN translation is applied in both ingress and egress sides of the layer 2 trunk on the port. It makes the traffic arriving on the VLAN with this VLAN ID to be mapped to or tagged with the corresponding instance of cvtPortTranslatedVlan on the port. It also causes all the traffic internally tagged with the corresponding instance of cvtPortTranslatedVlan and leaving the trunk port to be tagged with the VLAN of this VLAN ID.')
cvtPortTranslatedVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtPortTranslatedVlan.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslatedVlan.setDescription('The VLAN translation is applied in both ingress and egress sides of the Layer 2 trunk on the port. It makes the traffic arriving on the VLAN with the corresponding instance of cvtPortOriginalVlan on the device to be mapped to or tagged with the VLAN of this VLAN ID. It also causes all the traffic internally tagged with the VLAN of this VLAN ID and leaving the trunk port to be tagged with the corresponding instance of cvtPortOriginalVlan on the port.')
cvtPortTranslationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 411, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvtPortTranslationStatus.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationStatus.setDescription("The status of this conceptual row for the VLAN translation on the specific port. Once a row becomes active, value in any other column within such row cannot be modified. When this object is set to 'createAndGo' and the number of the existing rows for a specific physical port exceeds cvtPortTranslationMax of this port in cvtPortConfigTable, agent returns 'resourceUnavailable'.")
cvtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1))
cvtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 1, 1)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationGroup"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtMIBCompliance = cvtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvtMIBCompliance.setDescription('The compliance statement for trunk port VLAN translation implementations.')
cvtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2))
cvtGlobalTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 1)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationMax"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslatedVlan"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationEffective"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtGlobalTranslationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtGlobalTranslationGroup = cvtGlobalTranslationGroup.setStatus('current')
if mibBuilder.loadTexts: cvtGlobalTranslationGroup.setDescription('A collection of objects providing the device level VLAN translation ability on the device.')
cvtPortTranslationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 411, 2, 2, 2)).setObjects(("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationEnabled"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationMax"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslatedVlan"), ("CISCO-VLAN-TRANSLATION-MIB", "cvtPortTranslationStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvtPortTranslationGroup = cvtPortTranslationGroup.setStatus('current')
if mibBuilder.loadTexts: cvtPortTranslationGroup.setDescription('A collection of objects providing the port level VLAN translation ability on the device.')
mibBuilder.exportSymbols("CISCO-VLAN-TRANSLATION-MIB", cvtGlobalOriginalVlan=cvtGlobalOriginalVlan, cvtPortOriginalVlan=cvtPortOriginalVlan, cvtGlobalTranslationMax=cvtGlobalTranslationMax, cvtPortTranslationGroup=cvtPortTranslationGroup, ciscoVlanTranslationMIBNotifs=ciscoVlanTranslationMIBNotifs, cvtGlobalTranslation=cvtGlobalTranslation, PYSNMP_MODULE_ID=ciscoVlanTranslationMIB, cvtGlobalTranslationEffective=cvtGlobalTranslationEffective, cvtPortTranslationTable=cvtPortTranslationTable, cvtPortTranslationStatus=cvtPortTranslationStatus, ciscoVlanTranslationMIBObjects=ciscoVlanTranslationMIBObjects, cvtPortTranslationEnabled=cvtPortTranslationEnabled, ciscoVlanTranslationMIBConform=ciscoVlanTranslationMIBConform, ciscoVlanTranslationMIB=ciscoVlanTranslationMIB, cvtMIBCompliances=cvtMIBCompliances, cvtMIBGroups=cvtMIBGroups, cvtPortConfigTable=cvtPortConfigTable, cvtGlobalTranslationStatus=cvtGlobalTranslationStatus, cvtPortTranslatedVlan=cvtPortTranslatedVlan, cvtGlobalTranslatedVlan=cvtGlobalTranslatedVlan, cvtPortTranslationMax=cvtPortTranslationMax, cvtPortBasedTranslation=cvtPortBasedTranslation, cvtPortConfigEntry=cvtPortConfigEntry, cvtPortTranslationEntry=cvtPortTranslationEntry, cvtMIBCompliance=cvtMIBCompliance, cvtGlobalTranslationTable=cvtGlobalTranslationTable, cvtGlobalTranslationGroup=cvtGlobalTranslationGroup, cvtGlobalTranslationEntry=cvtGlobalTranslationEntry)
