#
# PySNMP MIB module ATM-REROUTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-REROUTING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmVclVpi, atmVplVpi, atmVclVci = mibBuilder.importSymbols("ATM-MIB", "atmVclVpi", "atmVplVpi", "atmVclVci")
AtmAddr, = mibBuilder.importSymbols("ATM-TC-MIB", "AtmAddr")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ObjectIdentity, ModuleIdentity, enterprises, Bits, Counter64, Counter32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ObjectIdentity", "ModuleIdentity", "enterprises", "Bits", "Counter64", "Counter32", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
atmfreroutingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1))
atmfreroutingMIB.setRevisions(('2001-04-26 00:00',))
if mibBuilder.loadTexts: atmfreroutingMIB.setLastUpdated('200104260000Z')
if mibBuilder.loadTexts: atmfreroutingMIB.setOrganization('The ATM Forum')
atmForum = MibIdentifier((1, 3, 6, 1, 4, 1, 353))
atmForumNetworkManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5))
atmfSignalling = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9))
atmfRerouting = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3))
reroutingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1))
class NetworkReroutingCapabilities(TextualConvention, Bits):
    reference = 'ATM Forum Domain-based rerouting 1.0'
    status = 'current'
    namedValues = NamedValues(("dbrHardRerouting", 0), ("dbrAsymmetricSoftRerouting", 1), ("dbrSymmetricSoftRerouting", 2))

class HardReroutingServicesClass(TextualConvention, Integer32):
    reference = 'Domain-based rerouting 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dbrInterDomainHardRerouting", 2), ("dbrIntraDomainHardRerouting", 3))

class SoftReroutingServicesClass(TextualConvention, Integer32):
    reference = 'Domain-based rerouting 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("dbrIntraDomainAsymmetricSoftRerouting", 2), ("dbrIntraDomainSymmetricSoftRerouting", 3))

class ReroutingNodeRole(TextualConvention, Integer32):
    reference = 'Domain-based rerouting 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("sourceNode", 2), ("destinationNode", 3))

class ReroutingState(TextualConvention, Integer32):
    reference = 'Domain-based rerouting 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("idle", 1), ("hardReroute", 2), ("softReroute", 3))

class ExtendedReroutingState(TextualConvention, Integer32):
    reference = 'Domain-based rerouting 1.0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("null", 1), ("reroutingIdle", 2), ("hardRerouteTriggered", 3), ("hardRerouteProceeding", 4), ("hardRerouteIndicated", 5), ("hardRerouteInitiated", 6), ("softRerouteTriggered", 7), ("softRerouteProceeding", 8), ("softRerouteInitiated", 9), ("awaitingSwitchover", 10))

reroutingBaseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1))
reroutingVersion = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unsupported", 1), ("version1point0", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVersion.setStatus('current')
reroutingCapabilitiesSupported = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 2), Bits().clone(namedValues=NamedValues(("dbrHardRerouting", 0), ("dbrAsymmetricSoftRerouting", 1), ("dbrSymmetricSoftRerouting", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingCapabilitiesSupported.setStatus('current')
reroutingHardReroutingTime = MibScalar((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: reroutingHardReroutingTime.setStatus('current')
reroutingFilterTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2), )
if mibBuilder.loadTexts: reroutingFilterTable.setStatus('current')
reroutingFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1), ).setIndexNames((0, "ATM-REROUTING-MIB", "reroutingFilterIndex"))
if mibBuilder.loadTexts: reroutingFilterEntry.setStatus('current')
reroutingFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: reroutingFilterIndex.setStatus('current')
reroutingFilterIfDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("in", 1), ("out", 2), ("both", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterIfDirection.setStatus('current')
reroutingFilterInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterInterface.setStatus('current')
reroutingFilterConnKind = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("other", 0), ("svcAndSpvcNotInitiator", 1), ("spvcInitiator", 2), ("svpAndSpvpNotInitiator", 3), ("spvpInitiator", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterConnKind.setStatus('current')
reroutingFilterServiceCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("cbr", 0), ("rtVbr", 1), ("nrtVbr", 2), ("abr", 3), ("ubr", 4), ("gfr", 5), ("other", 6)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterServiceCategory.setStatus('current')
reroutingFilterCallingPartyPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 6), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterCallingPartyPrefix.setStatus('current')
reroutingFilterCallingPartyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(152)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterCallingPartyLength.setStatus('current')
reroutingFilterCalledPartyPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 8), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterCalledPartyPrefix.setStatus('current')
reroutingFilterCalledPartyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 160)).clone(152)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterCalledPartyLength.setStatus('current')
reroutingFilterNetworkServicesAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 10), NetworkReroutingCapabilities()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterNetworkServicesAvailable.setStatus('current')
reroutingFilterHardReroutingServiceRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 11), HardReroutingServicesClass().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterHardReroutingServiceRequest.setStatus('current')
reroutingFilterSoftReroutingServiceRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 12), SoftReroutingServicesClass().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterSoftReroutingServiceRequest.setStatus('current')
reroutingFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: reroutingFilterRowStatus.setStatus('current')
reroutingVpTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3), )
if mibBuilder.loadTexts: reroutingVpTable.setStatus('current')
reroutingVpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVplVpi"))
if mibBuilder.loadTexts: reroutingVpEntry.setStatus('current')
reroutingVpNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 1), ReroutingNodeRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpNodeRole.setStatus('current')
reroutingVpRemoteNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 2), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpRemoteNodeAddress.setStatus('current')
reroutingVpHardReroutingServiceActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 3), HardReroutingServicesClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpHardReroutingServiceActivated.setStatus('current')
reroutingVpSoftReroutingServiceActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 4), SoftReroutingServicesClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpSoftReroutingServiceActivated.setStatus('current')
reroutingVpReroutingState = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 5), ReroutingState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpReroutingState.setStatus('current')
reroutingVpReroutingOperationSuccessCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpReroutingOperationSuccessCounter.setStatus('current')
reroutingVpReroutingOperationFailuresCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpReroutingOperationFailuresCounter.setStatus('current')
reroutingVpLocalIncarnationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpLocalIncarnationNumber.setStatus('current')
reroutingVpRemoteIncarnationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpRemoteIncarnationNumber.setStatus('current')
reroutingVpExtendedReroutingState = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 3, 1, 10), ExtendedReroutingState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVpExtendedReroutingState.setStatus('current')
reroutingVcTable = MibTable((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4), )
if mibBuilder.loadTexts: reroutingVcTable.setStatus('current')
reroutingVcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: reroutingVcEntry.setStatus('current')
reroutingVcNodeRole = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 1), ReroutingNodeRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcNodeRole.setStatus('current')
reroutingVcRemoteNodeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 2), AtmAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcRemoteNodeAddress.setStatus('current')
reroutingVcHardReroutingServiceActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 3), HardReroutingServicesClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcHardReroutingServiceActivated.setStatus('current')
reroutingVcSoftReroutingServiceActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 4), SoftReroutingServicesClass()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcSoftReroutingServiceActivated.setStatus('current')
reroutingVcReroutingState = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 5), ReroutingState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcReroutingState.setStatus('current')
reroutingVcReroutingOperationSuccessCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcReroutingOperationSuccessCounter.setStatus('current')
reroutingVcReroutingOperationFailuresCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcReroutingOperationFailuresCounter.setStatus('current')
reroutingVcLocalIncarnationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcLocalIncarnationNumber.setStatus('current')
reroutingVcRemoteIncarnationNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcRemoteIncarnationNumber.setStatus('current')
reroutingVcExtendedReroutingState = MibTableColumn((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 1, 4, 1, 10), ExtendedReroutingState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: reroutingVcExtendedReroutingState.setStatus('current')
reroutingMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2))
reroutingMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 1))
reroutingMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2))
reroutingMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 1, 1)).setObjects(("ATM-REROUTING-MIB", "reroutingBaseSwMinGroup"), ("ATM-REROUTING-MIB", "reroutingFilterSwMinGroup"), ("ATM-REROUTING-MIB", "reroutingVcSwMinGroup"), ("ATM-REROUTING-MIB", "reroutingBaseEsMinGroup"), ("ATM-REROUTING-MIB", "reroutingFilterEsMinGroup"), ("ATM-REROUTING-MIB", "reroutingVcEsMinGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingMIBCompliance = reroutingMIBCompliance.setStatus('current')
reroutingBaseSwMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 1)).setObjects(("ATM-REROUTING-MIB", "reroutingVersion"), ("ATM-REROUTING-MIB", "reroutingCapabilitiesSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingBaseSwMinGroup = reroutingBaseSwMinGroup.setStatus('current')
reroutingFilterSwMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 2)).setObjects(("ATM-REROUTING-MIB", "reroutingFilterIfDirection"), ("ATM-REROUTING-MIB", "reroutingFilterInterface"), ("ATM-REROUTING-MIB", "reroutingFilterNetworkServicesAvailable"), ("ATM-REROUTING-MIB", "reroutingFilterHardReroutingServiceRequest"), ("ATM-REROUTING-MIB", "reroutingFilterSoftReroutingServiceRequest"), ("ATM-REROUTING-MIB", "reroutingFilterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingFilterSwMinGroup = reroutingFilterSwMinGroup.setStatus('current')
reroutingVcSwMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 3)).setObjects(("ATM-REROUTING-MIB", "reroutingVcNodeRole"), ("ATM-REROUTING-MIB", "reroutingVcRemoteNodeAddress"), ("ATM-REROUTING-MIB", "reroutingVcHardReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVcSoftReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVcReroutingState"), ("ATM-REROUTING-MIB", "reroutingVcReroutingOperationSuccessCounter"), ("ATM-REROUTING-MIB", "reroutingVcReroutingOperationFailuresCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingVcSwMinGroup = reroutingVcSwMinGroup.setStatus('current')
reroutingBaseSwOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 4)).setObjects(("ATM-REROUTING-MIB", "reroutingHardReroutingTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingBaseSwOptionalGroup = reroutingBaseSwOptionalGroup.setStatus('current')
reroutingFilterSwOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 5)).setObjects(("ATM-REROUTING-MIB", "reroutingFilterConnKind"), ("ATM-REROUTING-MIB", "reroutingFilterServiceCategory"), ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyPrefix"), ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyLength"), ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyPrefix"), ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingFilterSwOptionalGroup = reroutingFilterSwOptionalGroup.setStatus('current')
reroutingVpSwOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 6)).setObjects(("ATM-REROUTING-MIB", "reroutingVpNodeRole"), ("ATM-REROUTING-MIB", "reroutingVpRemoteNodeAddress"), ("ATM-REROUTING-MIB", "reroutingVpHardReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVpSoftReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVpReroutingState"), ("ATM-REROUTING-MIB", "reroutingVpReroutingOperationSuccessCounter"), ("ATM-REROUTING-MIB", "reroutingVpReroutingOperationFailuresCounter"), ("ATM-REROUTING-MIB", "reroutingVpLocalIncarnationNumber"), ("ATM-REROUTING-MIB", "reroutingVpRemoteIncarnationNumber"), ("ATM-REROUTING-MIB", "reroutingVpExtendedReroutingState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingVpSwOptionalGroup = reroutingVpSwOptionalGroup.setStatus('current')
reroutingVcSwOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 7)).setObjects(("ATM-REROUTING-MIB", "reroutingVcLocalIncarnationNumber"), ("ATM-REROUTING-MIB", "reroutingVcRemoteIncarnationNumber"), ("ATM-REROUTING-MIB", "reroutingVcExtendedReroutingState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingVcSwOptionalGroup = reroutingVcSwOptionalGroup.setStatus('current')
reroutingBaseEsMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 8)).setObjects(("ATM-REROUTING-MIB", "reroutingVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingBaseEsMinGroup = reroutingBaseEsMinGroup.setStatus('current')
reroutingFilterEsMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 9)).setObjects(("ATM-REROUTING-MIB", "reroutingFilterIfDirection"), ("ATM-REROUTING-MIB", "reroutingFilterInterface"), ("ATM-REROUTING-MIB", "reroutingFilterHardReroutingServiceRequest"), ("ATM-REROUTING-MIB", "reroutingFilterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingFilterEsMinGroup = reroutingFilterEsMinGroup.setStatus('current')
reroutingVcEsMinGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 10)).setObjects(("ATM-REROUTING-MIB", "reroutingVcHardReroutingServiceActivated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingVcEsMinGroup = reroutingVcEsMinGroup.setStatus('current')
reroutingFilterEsOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 11)).setObjects(("ATM-REROUTING-MIB", "reroutingFilterConnKind"), ("ATM-REROUTING-MIB", "reroutingFilterServiceCategory"), ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyPrefix"), ("ATM-REROUTING-MIB", "reroutingFilterCallingPartyLength"), ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyPrefix"), ("ATM-REROUTING-MIB", "reroutingFilterCalledPartyLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingFilterEsOptionalGroup = reroutingFilterEsOptionalGroup.setStatus('current')
reroutingVpEsOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 353, 5, 9, 3, 1, 2, 2, 12)).setObjects(("ATM-REROUTING-MIB", "reroutingVpHardReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVpSoftReroutingServiceActivated"), ("ATM-REROUTING-MIB", "reroutingVcSoftReroutingServiceActivated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    reroutingVpEsOptionalGroup = reroutingVpEsOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("ATM-REROUTING-MIB", reroutingVcEsMinGroup=reroutingVcEsMinGroup, reroutingVcLocalIncarnationNumber=reroutingVcLocalIncarnationNumber, reroutingVcSoftReroutingServiceActivated=reroutingVcSoftReroutingServiceActivated, atmfSignalling=atmfSignalling, reroutingVpExtendedReroutingState=reroutingVpExtendedReroutingState, ReroutingNodeRole=ReroutingNodeRole, reroutingVcReroutingOperationFailuresCounter=reroutingVcReroutingOperationFailuresCounter, reroutingVersion=reroutingVersion, reroutingVpEsOptionalGroup=reroutingVpEsOptionalGroup, reroutingFilterEsMinGroup=reroutingFilterEsMinGroup, reroutingFilterTable=reroutingFilterTable, reroutingVcEntry=reroutingVcEntry, reroutingFilterIfDirection=reroutingFilterIfDirection, reroutingFilterConnKind=reroutingFilterConnKind, reroutingVcExtendedReroutingState=reroutingVcExtendedReroutingState, PYSNMP_MODULE_ID=atmfreroutingMIB, reroutingVcSwOptionalGroup=reroutingVcSwOptionalGroup, reroutingVpRemoteNodeAddress=reroutingVpRemoteNodeAddress, reroutingVpSwOptionalGroup=reroutingVpSwOptionalGroup, ReroutingState=ReroutingState, ExtendedReroutingState=ExtendedReroutingState, reroutingFilterRowStatus=reroutingFilterRowStatus, reroutingVpEntry=reroutingVpEntry, reroutingVcReroutingOperationSuccessCounter=reroutingVcReroutingOperationSuccessCounter, reroutingFilterCalledPartyPrefix=reroutingFilterCalledPartyPrefix, reroutingFilterInterface=reroutingFilterInterface, reroutingVpRemoteIncarnationNumber=reroutingVpRemoteIncarnationNumber, reroutingFilterSwMinGroup=reroutingFilterSwMinGroup, atmfRerouting=atmfRerouting, reroutingVpReroutingState=reroutingVpReroutingState, reroutingVpReroutingOperationFailuresCounter=reroutingVpReroutingOperationFailuresCounter, reroutingFilterCallingPartyPrefix=reroutingFilterCallingPartyPrefix, reroutingMIBCompliances=reroutingMIBCompliances, reroutingBaseSwOptionalGroup=reroutingBaseSwOptionalGroup, reroutingVpNodeRole=reroutingVpNodeRole, reroutingFilterSwOptionalGroup=reroutingFilterSwOptionalGroup, reroutingFilterEsOptionalGroup=reroutingFilterEsOptionalGroup, reroutingVcTable=reroutingVcTable, reroutingFilterCalledPartyLength=reroutingFilterCalledPartyLength, reroutingVpReroutingOperationSuccessCounter=reroutingVpReroutingOperationSuccessCounter, reroutingVpHardReroutingServiceActivated=reroutingVpHardReroutingServiceActivated, reroutingCapabilitiesSupported=reroutingCapabilitiesSupported, reroutingVpLocalIncarnationNumber=reroutingVpLocalIncarnationNumber, reroutingVpSoftReroutingServiceActivated=reroutingVpSoftReroutingServiceActivated, reroutingVcHardReroutingServiceActivated=reroutingVcHardReroutingServiceActivated, atmForumNetworkManagement=atmForumNetworkManagement, reroutingMIBObjects=reroutingMIBObjects, reroutingFilterNetworkServicesAvailable=reroutingFilterNetworkServicesAvailable, atmForum=atmForum, NetworkReroutingCapabilities=NetworkReroutingCapabilities, HardReroutingServicesClass=HardReroutingServicesClass, reroutingBaseSwMinGroup=reroutingBaseSwMinGroup, reroutingBaseGroup=reroutingBaseGroup, reroutingVcRemoteNodeAddress=reroutingVcRemoteNodeAddress, reroutingVcSwMinGroup=reroutingVcSwMinGroup, reroutingVcRemoteIncarnationNumber=reroutingVcRemoteIncarnationNumber, reroutingHardReroutingTime=reroutingHardReroutingTime, reroutingFilterEntry=reroutingFilterEntry, reroutingMIBGroups=reroutingMIBGroups, reroutingMIBCompliance=reroutingMIBCompliance, SoftReroutingServicesClass=SoftReroutingServicesClass, reroutingBaseEsMinGroup=reroutingBaseEsMinGroup, atmfreroutingMIB=atmfreroutingMIB, reroutingFilterServiceCategory=reroutingFilterServiceCategory, reroutingFilterSoftReroutingServiceRequest=reroutingFilterSoftReroutingServiceRequest, reroutingFilterIndex=reroutingFilterIndex, reroutingFilterHardReroutingServiceRequest=reroutingFilterHardReroutingServiceRequest, reroutingVcReroutingState=reroutingVcReroutingState, reroutingVcNodeRole=reroutingVcNodeRole, reroutingVpTable=reroutingVpTable, reroutingFilterCallingPartyLength=reroutingFilterCallingPartyLength, reroutingMIBConformance=reroutingMIBConformance)
