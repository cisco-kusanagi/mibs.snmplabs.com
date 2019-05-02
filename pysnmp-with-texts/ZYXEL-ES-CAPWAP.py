#
# PySNMP MIB module ZYXEL-ES-CAPWAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ES-CAPWAP
# Produced by pysmi-0.3.4 at Wed May  1 15:49:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, TimeTicks, NotificationType, ModuleIdentity, Unsigned32, Bits, Gauge32, Counter32, IpAddress, Counter64, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "Counter32", "IpAddress", "Counter64", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
esCAPWAP = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3))
if mibBuilder.loadTexts: esCAPWAP.setLastUpdated('201010060000Z')
if mibBuilder.loadTexts: esCAPWAP.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: esCAPWAP.setContactInfo('')
if mibBuilder.loadTexts: esCAPWAP.setDescription('The subtree for CAPWAP information')
capwapInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1))
if mibBuilder.loadTexts: capwapInfo.setStatus('current')
if mibBuilder.loadTexts: capwapInfo.setDescription('The subtree for CAPWAP')
capwapTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2))
if mibBuilder.loadTexts: capwapTraps.setStatus('current')
if mibBuilder.loadTexts: capwapTraps.setDescription('The subtree for CAPWAP')
capwapOnlineAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapOnlineAP.setStatus('current')
if mibBuilder.loadTexts: capwapOnlineAP.setDescription('Capwap online AP. ')
capwapOfflineAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapOfflineAP.setStatus('current')
if mibBuilder.loadTexts: capwapOfflineAP.setDescription('Capwap offline AP. ')
capwapUnMgntAP = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapUnMgntAP.setStatus('current')
if mibBuilder.loadTexts: capwapUnMgntAP.setDescription('Capwap unmanagment AP. ')
capwapTotalStation = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capwapTotalStation.setStatus('current')
if mibBuilder.loadTexts: capwapTotalStation.setDescription('Total stations in all AP. ')
capwapTrapsControl = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: capwapTrapsControl.setStatus('current')
if mibBuilder.loadTexts: capwapTrapsControl.setDescription('Controls capwap group traps enable or disable.')
capwapTrapsItems = ObjectIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2))
if mibBuilder.loadTexts: capwapTrapsItems.setStatus('current')
if mibBuilder.loadTexts: capwapTrapsItems.setDescription('The subtree for CAPWAP')
capwapWTPOnline = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 1))
if mibBuilder.loadTexts: capwapWTPOnline.setStatus('current')
if mibBuilder.loadTexts: capwapWTPOnline.setDescription('WTP online notification. ')
capwapWTPOffline = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 3, 2, 2, 2))
if mibBuilder.loadTexts: capwapWTPOffline.setStatus('current')
if mibBuilder.loadTexts: capwapWTPOffline.setDescription('WTP offline notification. ')
mibBuilder.exportSymbols("ZYXEL-ES-CAPWAP", PYSNMP_MODULE_ID=esCAPWAP, capwapUnMgntAP=capwapUnMgntAP, capwapWTPOffline=capwapWTPOffline, capwapOnlineAP=capwapOnlineAP, capwapTotalStation=capwapTotalStation, esCAPWAP=esCAPWAP, capwapTrapsControl=capwapTrapsControl, capwapWTPOnline=capwapWTPOnline, capwapInfo=capwapInfo, capwapTrapsItems=capwapTrapsItems, capwapOfflineAP=capwapOfflineAP, capwapTraps=capwapTraps)
