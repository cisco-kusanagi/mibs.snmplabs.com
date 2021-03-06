#
# PySNMP MIB module APPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
appExt, = mibBuilder.importSymbols("APENT-MIB", "appExt")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, Counter64, Counter32, Gauge32, Unsigned32, IpAddress, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter64", "Counter32", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
apAppMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 32, 1))
if mibBuilder.loadTexts: apAppMib.setLastUpdated('9802052000Z')
if mibBuilder.loadTexts: apAppMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apAppMib.setContactInfo('Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apAppMib.setDescription('This MIB module describes the ArrowPoint enterprise MIB support for App')
apAppSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2), )
if mibBuilder.loadTexts: apAppSessionTable.setStatus('current')
if mibBuilder.loadTexts: apAppSessionTable.setDescription('A table of App Sessions.')
apAppSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1), ).setIndexNames((0, "APPEXT-MIB", "apAppIpAddr"))
if mibBuilder.loadTexts: apAppSessionEntry.setStatus('current')
if mibBuilder.loadTexts: apAppSessionEntry.setDescription('ArrowPoint App table extensions')
apAppIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppIpAddr.setStatus('current')
if mibBuilder.loadTexts: apAppIpAddr.setDescription('The Interface IP Address of Peer')
apAppAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("authNone", 0), ("authChallenge", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppAuthType.setStatus('current')
if mibBuilder.loadTexts: apAppAuthType.setDescription('The type of Authentication performed on Peer')
apAppEncryptType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("encryptNone", 0), ("encryptMd5hash", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppEncryptType.setStatus('current')
if mibBuilder.loadTexts: apAppEncryptType.setDescription('The type of Encryption performed with Peer')
apAppKalFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(14, 900)).clone(14)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppKalFreq.setStatus('current')
if mibBuilder.loadTexts: apAppKalFreq.setDescription('Keep alive timer interval (seconds). Default is 14 sec.')
apAppSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppSecret.setStatus('current')
if mibBuilder.loadTexts: apAppSecret.setDescription('The secret authentication and encryption')
apAppPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppPktsTx.setStatus('current')
if mibBuilder.loadTexts: apAppPktsTx.setDescription('Count of the number of APP packets transmitted.')
apAppPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppPktsRx.setStatus('current')
if mibBuilder.loadTexts: apAppPktsRx.setDescription('Count of the number of APP packets received.')
apAppSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("stopped", 0), ("init", 1), ("opened", 2), ("auth", 3), ("up", 4), ("down", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apAppSessionState.setStatus('current')
if mibBuilder.loadTexts: apAppSessionState.setDescription('The current State of the Session')
apAppRcmdEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("rcmdEnable", 0), ("rcmdDisable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppRcmdEnable.setStatus('current')
if mibBuilder.loadTexts: apAppRcmdEnable.setDescription('Determines if remote CLI cmds are permitted on this Peer')
apAppSessionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 32, 2, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: apAppSessionStatus.setStatus('current')
if mibBuilder.loadTexts: apAppSessionStatus.setDescription('Status entry for this row')
apAppEnable = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 32, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apAppEnable.setStatus('current')
if mibBuilder.loadTexts: apAppEnable.setDescription('Parameter to enable or disable App functionality.')
apAppPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 32, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5001)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apAppPortNumber.setStatus('current')
if mibBuilder.loadTexts: apAppPortNumber.setDescription('The Port Number for the APP Protocol')
apAppMaxFrameSize = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 32, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10240, 65535)).clone(10240)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apAppMaxFrameSize.setStatus('current')
if mibBuilder.loadTexts: apAppMaxFrameSize.setDescription('The maximum frame size allowed by the APP Protocol')
mibBuilder.exportSymbols("APPEXT-MIB", apAppKalFreq=apAppKalFreq, apAppEncryptType=apAppEncryptType, apAppPortNumber=apAppPortNumber, apAppEnable=apAppEnable, apAppMib=apAppMib, apAppSessionEntry=apAppSessionEntry, apAppPktsTx=apAppPktsTx, apAppSessionState=apAppSessionState, apAppPktsRx=apAppPktsRx, apAppRcmdEnable=apAppRcmdEnable, apAppMaxFrameSize=apAppMaxFrameSize, PYSNMP_MODULE_ID=apAppMib, apAppSecret=apAppSecret, apAppSessionStatus=apAppSessionStatus, apAppSessionTable=apAppSessionTable, apAppIpAddr=apAppIpAddr, apAppAuthType=apAppAuthType)
