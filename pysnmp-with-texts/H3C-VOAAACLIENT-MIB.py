#
# PySNMP MIB module H3C-VOAAACLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOAAACLIENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Unsigned32, MibIdentifier, Counter64, Counter32, Integer32, TimeTicks, Bits, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "Counter32", "Integer32", "TimeTicks", "Bits", "NotificationType", "ModuleIdentity")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
h3cVoiceAAAClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9))
h3cVoiceAAAClient.setRevisions(('2006-03-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVoiceAAAClient.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cVoiceAAAClient.setLastUpdated('200603270000Z')
if mibBuilder.loadTexts: h3cVoiceAAAClient.setOrganization('Huawei-3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cVoiceAAAClient.setContactInfo('PLAT Team Huawei-3Com Technologies Co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cVoiceAAAClient.setDescription("This MIB file defines the voice AAA client MIB for remote dialing users' Authentication, Authorization and Accounting.")
h3cVoAAAClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1))
h3cVoAAAClientCfgObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1))
h3cVoAAAGwAuthenDid = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoAAAGwAuthenDid.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAuthenDid.setDescription('Enable or disable the function of authentication for Direct Inward Dialing.')
h3cVoAAAGwAuthorDid = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoAAAGwAuthorDid.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAuthorDid.setDescription('Enable or disable the function of authorization for Direct Inward Dialing on condition that the function of authentication is enabled.')
h3cVoAAAGwAccountingDid = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoAAAGwAccountingDid.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccountingDid.setDescription('Enable or disable the function of accounting for Direct Inward Dialing.')
h3cVoAAAGwAccountMethod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("startAck", 1), ("startNoAck", 2), ("stopOnly", 3))).clone('startNoAck')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoAAAGwAccountMethod.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccountMethod.setDescription('Specify the sending mode of accounting packets of this gateway. startAck: send starting and stopping accounting packets and wait for the acknowledge of RADIUS server. startNoAck: send starting and stopping accounting packets without waiting for the acknowledge of RADIUS server. stopOnly: send stopping accounting packets and wait for the acknowledge of RADIUS server.')
h3cVoAAAGwAccessNumberTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2), )
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumberTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumberTable.setDescription('The table contains the information of the AAA access number for Two-stage Dialing, which includes the configuration of authentication, authorization, accounting, the dialing process, the length of card number, the length of password , the redialing times.')
h3cVoAAAGwAccessNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1), ).setIndexNames((0, "H3C-VOAAACLIENT-MIB", "h3cVoAAAGwAccessNumber"))
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumberEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumberEntry.setDescription('The information of the access number.')
h3cVoAAAGwAccessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31)))
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccessNumber.setDescription("The access number of the AAA client. The access number can be composed of digits, wildcards or the letter 'T'. If digits, wildcards and the letter 'T' are all included in an access number, the wildcards must follow digits and appear at the end, and 'T' must be the last character and appear only once. In addition, an access number can include only wildcards, or only one 'T'.")
h3cVoAAAGwAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwAuthentication.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAuthentication.setDescription('Enable or disable the function of authentication for Two-stage Dialing.')
h3cVoAAAGwAuthorization = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwAuthorization.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAuthorization.setDescription('Enable or disable the function of authorization for Two-stage Dialing on condition that the function of authentication is enabled.')
h3cVoAAAGwAccounting = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 4), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwAccounting.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwAccounting.setDescription('Enable or disable the function of accounting for Two-stage Dialing.')
h3cVoAAAGwProcessConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("callerNumber", 1), ("cardNumber", 2), ("callerNumIvr", 3))).clone('callerNumIvr')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwProcessConfig.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwProcessConfig.setDescription("The dialing process type of this access number. callerNumber: caller number dialing process without IVR (Interactive Voice Reponse), that is, caller number's authentication for Two-stage Dialing process without IVR. cardNumber: card number dialing process with IVR, that is, card number and password's authentication for Two-stage Dialing process with IVR. callerNumIvr: caller number dialing process with IVR, that is, caller number's authentication for Two-stage Dialing process with IVR.")
h3cVoAAAGwCardDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(12)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwCardDigit.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwCardDigit.setDescription('The length of card number only for the cardNumber dialing process.')
h3cVoAAAGwPasswordDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwPasswordDigit.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwPasswordDigit.setDescription('The length of password only for the cardNumber dialing process.')
h3cVoAAAGwRedialTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwRedialTimes.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwRedialTimes.setDescription('The redialing times of inputing card number or password or called number for the cardNumber dialing process, or the redialing times of inputing called number for the callerNumIvr dialing process.')
h3cVoAAAGwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 9, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVoAAAGwRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVoAAAGwRowStatus.setDescription('The row status of this table.')
mibBuilder.exportSymbols("H3C-VOAAACLIENT-MIB", h3cVoAAAGwAuthorDid=h3cVoAAAGwAuthorDid, h3cVoAAAGwAccessNumberTable=h3cVoAAAGwAccessNumberTable, h3cVoAAAGwRedialTimes=h3cVoAAAGwRedialTimes, h3cVoAAAGwPasswordDigit=h3cVoAAAGwPasswordDigit, h3cVoAAAGwAccountMethod=h3cVoAAAGwAccountMethod, h3cVoAAAGwAccountingDid=h3cVoAAAGwAccountingDid, h3cVoAAAClientObjects=h3cVoAAAClientObjects, h3cVoiceAAAClient=h3cVoiceAAAClient, h3cVoAAAGwProcessConfig=h3cVoAAAGwProcessConfig, h3cVoAAAGwAccessNumber=h3cVoAAAGwAccessNumber, h3cVoAAAGwAuthorization=h3cVoAAAGwAuthorization, h3cVoAAAGwRowStatus=h3cVoAAAGwRowStatus, PYSNMP_MODULE_ID=h3cVoiceAAAClient, h3cVoAAAGwAccounting=h3cVoAAAGwAccounting, h3cVoAAAGwCardDigit=h3cVoAAAGwCardDigit, h3cVoAAAClientCfgObjects=h3cVoAAAClientCfgObjects, h3cVoAAAGwAuthenDid=h3cVoAAAGwAuthenDid, h3cVoAAAGwAuthentication=h3cVoAAAGwAuthentication, h3cVoAAAGwAccessNumberEntry=h3cVoAAAGwAccessNumberEntry)
