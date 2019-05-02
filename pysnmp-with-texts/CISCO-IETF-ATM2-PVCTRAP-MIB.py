#
# PySNMP MIB module CISCO-IETF-ATM2-PVCTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-ATM2-PVCTRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
atmVclVci, atmVclVpi, atmInterfaceConfEntry = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi", "atmInterfaceConfEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Counter32, IpAddress, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Unsigned32, iso, Integer32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Counter32", "IpAddress", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Unsigned32", "iso", "Integer32", "ModuleIdentity", "TimeTicks")
TextualConvention, TimeStamp, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "TruthValue")
ciscoIetfAtm2PvctrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 29))
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setLastUpdated('9802030000Z')
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoIetfAtm2PvctrapMIB.setDescription('This MIB Module is a supplement to the ATM-MIB.')
atm2MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 1))
atm2MIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2))
atmInterfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14), )
if mibBuilder.loadTexts: atmInterfaceExtTable.setStatus('current')
if mibBuilder.loadTexts: atmInterfaceExtTable.setDescription('This table contains ATM interface monitoring information not defined in the atmInterfaceConfTable from the ATM-MIB.')
atmInterfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1), )
atmInterfaceConfEntry.registerAugmentions(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmInterfaceExtEntry"))
atmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
if mibBuilder.loadTexts: atmInterfaceExtEntry.setStatus('current')
if mibBuilder.loadTexts: atmInterfaceExtEntry.setDescription('An entry extends the atmInterfaceConfEntry defined in ATM MIB. Each entry corresponds to an ATM interface.')
atmIntfPvcFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmIntfPvcFailures.setStatus('current')
if mibBuilder.loadTexts: atmIntfPvcFailures.setDescription('The number of times the operational status of a PVCL on this interface has gone down.')
atmIntfCurrentlyFailingPVcls = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 22), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmIntfCurrentlyFailingPVcls.setStatus('current')
if mibBuilder.loadTexts: atmIntfCurrentlyFailingPVcls.setDescription("The current number of VCLs on this interface for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'.")
atmIntfPvcFailuresTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 23), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmIntfPvcFailuresTrapEnable.setStatus('current')
if mibBuilder.loadTexts: atmIntfPvcFailuresTrapEnable.setDescription('Allows the generation of traps in response to PVCL failures on this interface.')
atmIntfPvcNotificationInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(30)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmIntfPvcNotificationInterval.setStatus('current')
if mibBuilder.loadTexts: atmIntfPvcNotificationInterval.setDescription('The minimum interval between the sending of cIntfPvcFailuresTrap notifications for this interface.')
atmPreviouslyFailedPVclInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 14, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPreviouslyFailedPVclInterval.setStatus('current')
if mibBuilder.loadTexts: atmPreviouslyFailedPVclInterval.setDescription('The interval for storing the failed time in atmPreviouslyFailedPVclTimeStamp')
atmCurrentlyFailingPVclTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21), )
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTable.setStatus('current')
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTable.setDescription("A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and an atmVclOperStatus with a value other than `up'.")
atmCurrentlyFailingPVclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: atmCurrentlyFailingPVclEntry.setStatus('current')
if mibBuilder.loadTexts: atmCurrentlyFailingPVclEntry.setDescription("Each entry in this table represents a VCL for which the atmVclRowStatus is `active', the atmVclConnKind is `pvc', and the atmVclOperStatus is other than `up'.")
atmCurrentlyFailingPVclTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTimeStamp.setStatus('current')
if mibBuilder.loadTexts: atmCurrentlyFailingPVclTimeStamp.setDescription('The time at which this PVCL began to fail.')
atmPreviouslyFailedPVclTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 29, 1, 21, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPreviouslyFailedPVclTimeStamp.setStatus('current')
if mibBuilder.loadTexts: atmPreviouslyFailedPVclTimeStamp.setDescription('The time at which this PVCL began to fail during the PVC Notification interval.')
atmPvcTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1))
atmPvcTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0))
atmIntfPvcFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 29, 2, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"))
if mibBuilder.loadTexts: atmIntfPvcFailuresTrap.setStatus('current')
if mibBuilder.loadTexts: atmIntfPvcFailuresTrap.setDescription('A notification indicating that one or more PVCLs on this interface has failed since the last cIntfPvcFailuresTrap was sent. If this trap has not been sent for the last cIntfPvcNotificationInterval, then it will be sent on the next increment of cIntfPvcFailures.')
atm2MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3))
atm2MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1))
atm2MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2))
atm2MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 2, 1)).setObjects(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmSwitchServcHostGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atm2MIBCompliance = atm2MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: atm2MIBCompliance.setDescription('The compliance statement for SNMP entities which implement PVC traps.')
atmSwitchServcHostGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 29, 3, 1, 1)).setObjects(("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailures"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfCurrentlyFailingPVcls"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcFailuresTrapEnable"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmIntfPvcNotificationInterval"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclInterval"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmCurrentlyFailingPVclTimeStamp"), ("CISCO-IETF-ATM2-PVCTRAP-MIB", "atmPreviouslyFailedPVclTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    atmSwitchServcHostGroup = atmSwitchServcHostGroup.setStatus('current')
if mibBuilder.loadTexts: atmSwitchServcHostGroup.setDescription('A collection of objects providing information for a Switch/Service/Host that implements PVC traps for an ATM interfaces.')
mibBuilder.exportSymbols("CISCO-IETF-ATM2-PVCTRAP-MIB", atmSwitchServcHostGroup=atmSwitchServcHostGroup, atm2MIBGroups=atm2MIBGroups, atmIntfPvcFailuresTrapEnable=atmIntfPvcFailuresTrapEnable, atmInterfaceExtTable=atmInterfaceExtTable, PYSNMP_MODULE_ID=ciscoIetfAtm2PvctrapMIB, atmInterfaceExtEntry=atmInterfaceExtEntry, atmCurrentlyFailingPVclEntry=atmCurrentlyFailingPVclEntry, atmIntfCurrentlyFailingPVcls=atmIntfCurrentlyFailingPVcls, atmPreviouslyFailedPVclTimeStamp=atmPreviouslyFailedPVclTimeStamp, ciscoIetfAtm2PvctrapMIB=ciscoIetfAtm2PvctrapMIB, atmCurrentlyFailingPVclTimeStamp=atmCurrentlyFailingPVclTimeStamp, atmIntfPvcFailuresTrap=atmIntfPvcFailuresTrap, atm2MIBConformance=atm2MIBConformance, atmIntfPvcNotificationInterval=atmIntfPvcNotificationInterval, atm2MIBObjects=atm2MIBObjects, atmPvcTrapsPrefix=atmPvcTrapsPrefix, atmPreviouslyFailedPVclInterval=atmPreviouslyFailedPVclInterval, atmCurrentlyFailingPVclTable=atmCurrentlyFailingPVclTable, atm2MIBCompliance=atm2MIBCompliance, atmIntfPvcFailures=atmIntfPvcFailures, atmPvcTraps=atmPvcTraps, atm2MIBTraps=atm2MIBTraps, atm2MIBCompliances=atm2MIBCompliances)
