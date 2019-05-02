#
# PySNMP MIB module HUAWEI-L2VPN-PW-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-L2VPN-PW-APS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:45:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
hwPWInterfaceIndex, = mibBuilder.importSymbols("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex")
HWL2VpnVcEncapsType, = mibBuilder.importSymbols("HUAWEI-VPLS-EXT-MIB", "HWL2VpnVcEncapsType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Bits, Counter64, TimeTicks, Gauge32, ObjectIdentity, MibIdentifier, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Bits", "Counter64", "TimeTicks", "Gauge32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hwL2vpnPwAps = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10))
hwL2vpnPwAps.setRevisions(('2013-05-13 12:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwL2vpnPwAps.setRevisionsDescriptions(('V2.11, add hwPwApsDegraded for PTN5900',))
if mibBuilder.loadTexts: hwL2vpnPwAps.setLastUpdated('201305131250Z')
if mibBuilder.loadTexts: hwL2vpnPwAps.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwL2vpnPwAps.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwL2vpnPwAps.setDescription('The HUAWEI-L2VPN-PW-APS-MIB contains objects to manage PW APS.')
hwL2Vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119))
hwPwApsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1))
hwPwApsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1), )
if mibBuilder.loadTexts: hwPwApsTable.setStatus('current')
if mibBuilder.loadTexts: hwPwApsTable.setDescription('This table provides the information of PW APS.')
hwPwApsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1), ).setIndexNames((0, "HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"))
if mibBuilder.loadTexts: hwPwApsEntry.setStatus('current')
if mibBuilder.loadTexts: hwPwApsEntry.setDescription('Provides the information of a PW APS entry.')
hwPwApsId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwPwApsId.setStatus('current')
if mibBuilder.loadTexts: hwPwApsId.setDescription('This object indicates the ID of the PW APS.')
hwPwApsRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("master", 1), ("slave", 2), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPwApsRole.setStatus('current')
if mibBuilder.loadTexts: hwPwApsRole.setDescription('This object indicates the role of the PW APS.')
hwPwApsRequestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("work", 1), ("protect", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPwApsRequestResult.setStatus('current')
if mibBuilder.loadTexts: hwPwApsRequestResult.setDescription('This object indicates the request result of the PW APS.')
hwPwApsState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 255))).clone(namedValues=NamedValues(("lo", 1), ("sfp", 2), ("fs", 3), ("sf", 4), ("sdp", 5), ("sd", 6), ("ms", 7), ("wtr", 8), ("exer", 9), ("rr", 10), ("dnr", 11), ("nr", 12), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPwApsState.setStatus('current')
if mibBuilder.loadTexts: hwPwApsState.setDescription('This object indicates the state of the PW APS.')
hwPwApsWorkState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("nondefect", 1), ("defect", 2), ("defectsd", 3), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPwApsWorkState.setStatus('current')
if mibBuilder.loadTexts: hwPwApsWorkState.setDescription('This object indicates the work state of the PW APS.')
hwPwApsProtectState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("nondefect", 1), ("defect", 2), ("defectsd", 3), ("unknown", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwPwApsProtectState.setStatus('current')
if mibBuilder.loadTexts: hwPwApsProtectState.setDescription('This object indicates the protect state of the PW APS.')
hwL2vpnPwApsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2))
hwPwApsTypeMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 1)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsTypeMismatch.setStatus('current')
if mibBuilder.loadTexts: hwPwApsTypeMismatch.setDescription('APS reported an alarm about the mismatch of the protection type.')
hwPwApsTypeMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 2)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsTypeMismatchClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsTypeMismatchClear.setDescription('APS reported an alarm about the rectification of the mismatch of the protection type.')
hwPwApsPathMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 3)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsPathMismatch.setStatus('current')
if mibBuilder.loadTexts: hwPwApsPathMismatch.setDescription('APS reported an alarm about the mismatch of the working and protection paths.')
hwPwApsPathMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 4)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsPathMismatchClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsPathMismatchClear.setDescription('APS reported an alarm about the rectification of the mismatch of the working and protection paths.')
hwPwApsSwitchFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 5)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsSwitchFail.setStatus('current')
if mibBuilder.loadTexts: hwPwApsSwitchFail.setDescription('APS reported an alarm about the inconsistent switching results on the local and remote ends.')
hwPwApsSwitchFailClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 6)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsSwitchFailClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsSwitchFailClear.setDescription('APS reported an alarm about the rectification of the inconsistency in switching results on the local and remote ends.')
hwPwApsLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 7)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsLost.setStatus('current')
if mibBuilder.loadTexts: hwPwApsLost.setDescription('APS reported a packet lost alarm.')
hwPwApsLostClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 8)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsLostClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsLostClear.setDescription('APS reported the clearing of the packet loss alarm.')
hwPwApsIdMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 9)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsIdMismatch.setStatus('current')
if mibBuilder.loadTexts: hwPwApsIdMismatch.setDescription('APS reported an ID mismatch alarm.')
hwPwApsIdMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 10)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsIdMismatchClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsIdMismatchClear.setDescription('APS reported the clearing of the ID mismatch alarm.')
hwPwApsBypassPwMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 11)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsBypassPwMismatch.setStatus('current')
if mibBuilder.loadTexts: hwPwApsBypassPwMismatch.setDescription('APS reported a bypass mismatch alarm.')
hwPwApsBypssPwMismatchClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 12)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsBypssPwMismatchClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsBypssPwMismatchClear.setDescription('APS reported the clearing of the bypass mismatch alarm.')
hwPwApsSwitchEvent = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 13)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRole"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRequestResult"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsState"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsWorkState"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsProtectState"))
if mibBuilder.loadTexts: hwPwApsSwitchEvent.setStatus('current')
if mibBuilder.loadTexts: hwPwApsSwitchEvent.setDescription('APS reported the event of switch.')
hwPwApsOutAge = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 14)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsOutAge.setStatus('current')
if mibBuilder.loadTexts: hwPwApsOutAge.setDescription('APS reported a PW out age alarm.')
hwPwApsOutAgeClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 15)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsOutAgeClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsOutAgeClear.setDescription('APS reported the clearing of the PW out age alarm.')
hwPwApsDegraded = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 16)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsDegraded.setStatus('current')
if mibBuilder.loadTexts: hwPwApsDegraded.setDescription('APS reported a PW degraded alarm.')
hwPwApsDegradedClear = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 2, 17)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-PWE3-MIB", "hwPWInterfaceIndex"))
if mibBuilder.loadTexts: hwPwApsDegradedClear.setStatus('current')
if mibBuilder.loadTexts: hwPwApsDegradedClear.setDescription('APS reported the clearing of the PW degraded alarm.')
hwL2vpnPwApsScalarsObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 3))
hwPwApsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4))
hwPwApsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 1))
hwPwApsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 1, 1)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsGroup"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPwApsMIBCompliance = hwPwApsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: hwPwApsMIBCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-L2VPN-PW-APS-MIB.')
hwPwApsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2))
hwPwApsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2, 1)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsId"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRole"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsRequestResult"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsState"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsWorkState"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsProtectState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPwApsGroup = hwPwApsGroup.setStatus('current')
if mibBuilder.loadTexts: hwPwApsGroup.setDescription('The PW APS group.')
hwPwApsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 10, 4, 2, 2)).setObjects(("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsTypeMismatch"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsTypeMismatchClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsPathMismatch"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsPathMismatchClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchFail"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchFailClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsLost"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsLostClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsIdMismatch"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsIdMismatchClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsBypassPwMismatch"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsBypssPwMismatchClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsSwitchEvent"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsOutAge"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsOutAgeClear"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsDegraded"), ("HUAWEI-L2VPN-PW-APS-MIB", "hwPwApsDegradedClear"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPwApsNotificationGroup = hwPwApsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwPwApsNotificationGroup.setDescription('The PW APS Notification group.')
mibBuilder.exportSymbols("HUAWEI-L2VPN-PW-APS-MIB", hwPwApsMIBGroups=hwPwApsMIBGroups, hwPwApsTypeMismatch=hwPwApsTypeMismatch, hwL2vpnPwAps=hwL2vpnPwAps, hwPwApsWorkState=hwPwApsWorkState, hwPwApsState=hwPwApsState, hwPwApsLost=hwPwApsLost, hwPwApsDegraded=hwPwApsDegraded, hwPwApsLostClear=hwPwApsLostClear, hwPwApsPathMismatchClear=hwPwApsPathMismatchClear, hwPwApsSwitchFailClear=hwPwApsSwitchFailClear, hwPwApsSwitchFail=hwPwApsSwitchFail, hwPwApsGroup=hwPwApsGroup, hwPwApsNotificationGroup=hwPwApsNotificationGroup, hwPwApsTypeMismatchClear=hwPwApsTypeMismatchClear, hwL2vpnPwApsTraps=hwL2vpnPwApsTraps, hwL2vpnPwApsScalarsObject=hwL2vpnPwApsScalarsObject, hwPwApsRequestResult=hwPwApsRequestResult, hwPwApsMIBConformance=hwPwApsMIBConformance, hwPwApsDegradedClear=hwPwApsDegradedClear, hwPwApsSwitchEvent=hwPwApsSwitchEvent, hwPwApsOutAgeClear=hwPwApsOutAgeClear, hwPwApsOutAge=hwPwApsOutAge, hwPwApsMIBCompliance=hwPwApsMIBCompliance, hwPwApsBypassPwMismatch=hwPwApsBypassPwMismatch, hwPwApsObjects=hwPwApsObjects, hwPwApsTable=hwPwApsTable, hwPwApsIdMismatch=hwPwApsIdMismatch, hwPwApsIdMismatchClear=hwPwApsIdMismatchClear, hwPwApsRole=hwPwApsRole, hwPwApsMIBCompliances=hwPwApsMIBCompliances, hwPwApsBypssPwMismatchClear=hwPwApsBypssPwMismatchClear, hwPwApsPathMismatch=hwPwApsPathMismatch, hwL2Vpn=hwL2Vpn, PYSNMP_MODULE_ID=hwL2vpnPwAps, hwPwApsId=hwPwApsId, hwPwApsProtectState=hwPwApsProtectState, hwPwApsEntry=hwPwApsEntry)
