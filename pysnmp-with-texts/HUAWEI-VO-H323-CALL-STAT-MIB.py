#
# PySNMP MIB module HUAWEI-VO-H323-CALL-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VO-H323-CALL-STAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
voice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "voice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Gauge32, Integer32, Unsigned32, ModuleIdentity, TimeTicks, Bits, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Gauge32", "Integer32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Bits", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwVoiceH323CallStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11))
hwVoiceH323CallStatMIB.setRevisions(('2004-04-08 13:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwVoiceH323CallStatMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwVoiceH323CallStatMIB.setLastUpdated('200410200000Z')
if mibBuilder.loadTexts: hwVoiceH323CallStatMIB.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwVoiceH323CallStatMIB.setContactInfo('PLAT Team Huawei 3Com Technologies co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: hwVoiceH323CallStatMIB.setDescription(' ')
hwVoH323CallStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1))
hwVoIPPH225StatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1))
hwVoSend_Setup = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 1), Counter32()).setLabel("hwVoSend-Setup").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_Setup.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_Setup.setDescription('setup message number send to peer.')
hwVoSend_CallProceeding = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 2), Counter32()).setLabel("hwVoSend-CallProceeding").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_CallProceeding.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_CallProceeding.setDescription('CallProceeding message number send to peer.')
hwVoSend_Alerting = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 3), Counter32()).setLabel("hwVoSend-Alerting").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_Alerting.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_Alerting.setDescription('Alerting message number send to peer.')
hwVoSend_Connect = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 4), Counter32()).setLabel("hwVoSend-Connect").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_Connect.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_Connect.setDescription('Connect message number send to peer.')
hwVoSend_ReleaseComplete = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 5), Counter32()).setLabel("hwVoSend-ReleaseComplete").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_ReleaseComplete.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_ReleaseComplete.setDescription('ReleaseComplete message number send to peer.')
hwVoSend_FacilityIndUserInput = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 6), Counter32()).setLabel("hwVoSend-FacilityIndUserInput").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityIndUserInput.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityIndUserInput.setDescription('FacilityIndUserInput message number send to peer.')
hwVoSend_FacilityTCSRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 7), Counter32()).setLabel("hwVoSend-FacilityTCSRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityTCSRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityTCSRequest.setDescription('FacilityTCSRequest message number send to peer.')
hwVoSend_FacilityTCSAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 8), Counter32()).setLabel("hwVoSend-FacilityTCSAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityTCSAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityTCSAck.setDescription('FacilityTCSAck message number send to peer.')
hwVoSend_FacilityTCSReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 9), Counter32()).setLabel("hwVoSend-FacilityTCSReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityTCSReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityTCSReject.setDescription('FacilityTCSReject message number send to peer.')
hwVoSend_FacilityOLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 10), Counter32()).setLabel("hwVoSend-FacilityOLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityOLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityOLCRequest.setDescription('FacilityOLCRequest message number send to peer.')
hwVoSend_FacilityOLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 11), Counter32()).setLabel("hwVoSend-FacilityOLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityOLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityOLCAck.setDescription('FacilityOLCAck message number send to peer.')
hwVoSend_FacilityOLCReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 12), Counter32()).setLabel("hwVoSend-FacilityOLCReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityOLCReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityOLCReject.setDescription('FacilityOLCReject message number send to peer.')
hwVoSend_FacilityMSDRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 13), Counter32()).setLabel("hwVoSend-FacilityMSDRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityMSDRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityMSDRequest.setDescription('FacilityMSDRequest message number send to peer.')
hwVoSend_FacilityMSDAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 14), Counter32()).setLabel("hwVoSend-FacilityMSDAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityMSDAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityMSDAck.setDescription('FacilityMSDAck message number send to peer.')
hwVoSend_FacilityMSDReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 15), Counter32()).setLabel("hwVoSend-FacilityMSDReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityMSDReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityMSDReject.setDescription('FacilityMSDReject message number send to peer.')
hwVoSend_FacilityCLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 16), Counter32()).setLabel("hwVoSend-FacilityCLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityCLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityCLCRequest.setDescription('FacilityCLCRequest message number send to peer.')
hwVoSend_FacilityCLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 17), Counter32()).setLabel("hwVoSend-FacilityCLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityCLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityCLCAck.setDescription('FacilityCLCAck message number send to peer.')
hwVoSend_FacilityStartH245 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 18), Counter32()).setLabel("hwVoSend-FacilityStartH245").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_FacilityStartH245.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_FacilityStartH245.setDescription('FacilityStartH245 message number send to peer.')
hwVoSend_ErrorH225Msg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 19), Counter32()).setLabel("hwVoSend-ErrorH225Msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_ErrorH225Msg.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_ErrorH225Msg.setDescription('Error 225 message number send to peer.')
hwVoRecv_Setup = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 20), Counter32()).setLabel("hwVoRecv-Setup").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_Setup.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_Setup.setDescription('Setup message number receive from peer.')
hwVoRecv_CallProceeding = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 21), Counter32()).setLabel("hwVoRecv-CallProceeding").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_CallProceeding.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_CallProceeding.setDescription('CallProceeding message number receive from peer.')
hwVoRecv_Alerting = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 22), Counter32()).setLabel("hwVoRecv-Alerting").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_Alerting.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_Alerting.setDescription('Alerting message number receive from peer.')
hwVoRecv_Connect = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 23), Counter32()).setLabel("hwVoRecv-Connect").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_Connect.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_Connect.setDescription('Connect message number receive from peer.')
hwVoRecv_ReleaseComplete = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 24), Counter32()).setLabel("hwVoRecv-ReleaseComplete").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_ReleaseComplete.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_ReleaseComplete.setDescription('ReleaseComplete message number receive from peer.')
hwVoRecv_Progress = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 25), Counter32()).setLabel("hwVoRecv-Progress").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_Progress.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_Progress.setDescription('Progress message number receive from peer.')
hwVoRecv_FacilityTCSRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 26), Counter32()).setLabel("hwVoRecv-FacilityTCSRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSRequest.setDescription('FacilityTCSRequest message number receive from peer.')
hwVoRecv_FacilityTCSAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 27), Counter32()).setLabel("hwVoRecv-FacilityTCSAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSAck.setDescription('FacilityTCSAck message number receive from peer.')
hwVoRecv_FacilityTCSReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 28), Counter32()).setLabel("hwVoRecv-FacilityTCSReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityTCSReject.setDescription('FacilityTCSReject message number receive from peer.')
hwVoRecv_FacilityOLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 29), Counter32()).setLabel("hwVoRecv-FacilityOLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCRequest.setDescription('FacilityOLCRequest message number receive from peer.')
hwVoRecv_FacilityOLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 30), Counter32()).setLabel("hwVoRecv-FacilityOLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCAck.setDescription('FacilityOLCAck message number receive from peer.')
hwVoRecv_FacilityOLCReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 31), Counter32()).setLabel("hwVoRecv-FacilityOLCReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityOLCReject.setDescription('FacilityOLCReject message number receive from peer.')
hwVoRecv_FacilityMSDRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 32), Counter32()).setLabel("hwVoRecv-FacilityMSDRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDRequest.setDescription('FacilityMSDRequest message number receive from peer.')
hwVoRecv_FacilityMSDAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 33), Counter32()).setLabel("hwVoRecv-FacilityMSDAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDAck.setDescription('FacilityMSDAck message number receive from peer.')
hwVoRecv_FacilityMSDReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 34), Counter32()).setLabel("hwVoRecv-FacilityMSDReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityMSDReject.setDescription('FacilityMSDReject message number receive from peer.')
hwVoRecv_FacilityCLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 35), Counter32()).setLabel("hwVoRecv-FacilityCLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityCLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityCLCRequest.setDescription('FacilityCLCRequest message number receive from peer.')
hwVoRecv_FacilityCLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 36), Counter32()).setLabel("hwVoRecv-FacilityCLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_FacilityCLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_FacilityCLCAck.setDescription('FacilityCLCAck message number receive from peer.')
hwVoRecv_UnknownH225Msg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 1, 37), Counter32()).setLabel("hwVoRecv-UnknownH225Msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_UnknownH225Msg.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_UnknownH225Msg.setDescription('Unknow 225 message number receive from peer.')
hwVoIPPH245StatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2))
hwVoSend_TCSRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 1), Counter32()).setLabel("hwVoSend-TCSRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_TCSRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_TCSRequest.setDescription('TCSRequest message number send to peer.')
hwVoSend_TCSAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 2), Counter32()).setLabel("hwVoSend-TCSAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_TCSAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_TCSAck.setDescription('TCSAck message number send to peer.')
hwVoSend_TCSReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 3), Counter32()).setLabel("hwVoSend-TCSReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_TCSReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_TCSReject.setDescription('TCSReject message number send to peer.')
hwVoSend_MSDRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 4), Counter32()).setLabel("hwVoSend-MSDRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_MSDRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_MSDRequest.setDescription('MSDRequest message number send to peer.')
hwVoSend_MSDAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 5), Counter32()).setLabel("hwVoSend-MSDAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_MSDAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_MSDAck.setDescription('MSDAck message number send to peer.')
hwVoSend_MSDReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 6), Counter32()).setLabel("hwVoSend-MSDReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_MSDReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_MSDReject.setDescription('MSDReject message number send to peer.')
hwVoSend_OLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 7), Counter32()).setLabel("hwVoSend-OLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_OLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_OLCRequest.setDescription('OLCRequest message number send to peer.')
hwVoSend_OLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 8), Counter32()).setLabel("hwVoSend-OLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_OLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_OLCAck.setDescription('OLCAck message number send to peer.')
hwVoSend_OLCReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 9), Counter32()).setLabel("hwVoSend-OLCReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_OLCReject.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_OLCReject.setDescription('OLCReject message number send to peer.')
hwVoSend_CLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 10), Counter32()).setLabel("hwVoSend-CLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_CLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_CLCRequest.setDescription('CLCRequest message number send to peer.')
hwVoSend_CLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 11), Counter32()).setLabel("hwVoSend-CLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_CLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_CLCAck.setDescription('CLCAck message number send to peer.')
hwVoSend_UserInput = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 12), Counter32()).setLabel("hwVoSend-UserInput").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_UserInput.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_UserInput.setDescription('UserInput message number send to peer.')
hwVoSend_ErrorH245Msg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 13), Counter32()).setLabel("hwVoSend-ErrorH245Msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_ErrorH245Msg.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_ErrorH245Msg.setDescription('Error 245 message number send to peer.')
hwVoRecv_TCSRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 14), Counter32()).setLabel("hwVoRecv-TCSRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_TCSRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_TCSRequest.setDescription('TCSRequest message number receive from peer.')
hwVoRecv_TCSAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 15), Counter32()).setLabel("hwVoRecv-TCSAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_TCSAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_TCSAck.setDescription('TCSAck message number receive from peer.')
hwVoRecv_TCSReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 16), Counter32()).setLabel("hwVoRecv-TCSReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_TCSReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_TCSReject.setDescription('TCSReject message number receive from peer.')
hwVoRecv_MSDRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 17), Counter32()).setLabel("hwVoRecv-MSDRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_MSDRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_MSDRequest.setDescription('MSDRequest message number receive from peer.')
hwVoRecv_MSDAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 18), Counter32()).setLabel("hwVoRecv-MSDAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_MSDAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_MSDAck.setDescription('MSDAck message number receive from peer.')
hwVoRecv_MSDReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 19), Counter32()).setLabel("hwVoRecv-MSDReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_MSDReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_MSDReject.setDescription('MSDReject message number receive from peer.')
hwVoRecv_OLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 20), Counter32()).setLabel("hwVoRecv-OLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_OLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_OLCRequest.setDescription('OLCRequest message number receive from peer.')
hwVoRecv_OLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 21), Counter32()).setLabel("hwVoRecv-OLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_OLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_OLCAck.setDescription('OLCAck message number receive from peer.')
hwVoRecv_OLCReject = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 22), Counter32()).setLabel("hwVoRecv-OLCReject").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_OLCReject.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_OLCReject.setDescription('OLCReject message number receive from peer.')
hwVoRecv_CLCRequest = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 23), Counter32()).setLabel("hwVoRecv-CLCRequest").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_CLCRequest.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_CLCRequest.setDescription('CLCRequest message number receive from peer.')
hwVoRecv_CLCAck = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 24), Counter32()).setLabel("hwVoRecv-CLCAck").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_CLCAck.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_CLCAck.setDescription('CLCAck message number receive from peer.')
hwVoRecv_UserInput = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 25), Counter32()).setLabel("hwVoRecv-UserInput").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_UserInput.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_UserInput.setDescription('UserInput message number receive from peer.')
hwVoRecv_UnknownH245Msg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 2, 26), Counter32()).setLabel("hwVoRecv-UnknownH245Msg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_UnknownH245Msg.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_UnknownH245Msg.setDescription('Unknow 245 message number receive from peer.')
hwVoIPPRASStatObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3))
hwVoSend_GRQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 1), Counter32()).setLabel("hwVoSend-GRQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_GRQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_GRQ.setDescription('GRQ message number send to peer.')
hwVoSend_RRQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 2), Counter32()).setLabel("hwVoSend-RRQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_RRQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_RRQ.setDescription('RRQ message number send to peer.')
hwVoSend_ARQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 3), Counter32()).setLabel("hwVoSend-ARQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_ARQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_ARQ.setDescription('ARQ message number send to peer.')
hwVoSend_BRQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 4), Counter32()).setLabel("hwVoSend-BRQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_BRQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_BRQ.setDescription('BRQ message number send to peer.')
hwVoSend_DRQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 5), Counter32()).setLabel("hwVoSend-DRQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_DRQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_DRQ.setDescription('DRQ message number send to peer.')
hwVoSend_URQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 6), Counter32()).setLabel("hwVoSend-URQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_URQ.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_URQ.setDescription('URQ message number send to peer.')
hwVoSend_UCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 7), Counter32()).setLabel("hwVoSend-UCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_UCF.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_UCF.setDescription('UCF message number send to peer.')
hwVoSend_IRR = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 8), Counter32()).setLabel("hwVoSend-IRR").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_IRR.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_IRR.setDescription('IRR message number send to peer.')
hwVoSend_ErrorRASMsg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 9), Counter32()).setLabel("hwVoSend-ErrorRASMsg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoSend_ErrorRASMsg.setStatus('current')
if mibBuilder.loadTexts: hwVoSend_ErrorRASMsg.setDescription('Error RAS message number send to peer.')
hwVoRecv_GCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 10), Counter32()).setLabel("hwVoRecv-GCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_GCF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_GCF.setDescription('GCF message number receive from peer.')
hwVoRecv_RCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 11), Counter32()).setLabel("hwVoRecv-RCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_RCF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_RCF.setDescription('RCF message number receive from peer.')
hwVoRecv_ACF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 12), Counter32()).setLabel("hwVoRecv-ACF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_ACF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_ACF.setDescription('ACF message number receive from peer.')
hwVoRecv_BCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 13), Counter32()).setLabel("hwVoRecv-BCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_BCF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_BCF.setDescription('BCF message number receive from peer.')
hwVoRecv_DCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 14), Counter32()).setLabel("hwVoRecv-DCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_DCF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_DCF.setDescription('DCF message number receive from peer.')
hwVoRecv_GRJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 15), Counter32()).setLabel("hwVoRecv-GRJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_GRJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_GRJ.setDescription('GRJ message number receive from peer.')
hwVoRecv_RRJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 16), Counter32()).setLabel("hwVoRecv-RRJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_RRJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_RRJ.setDescription('RRJ message number receive from peer.')
hwVoRecv_ARJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 17), Counter32()).setLabel("hwVoRecv-ARJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_ARJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_ARJ.setDescription('ARJ message number receive from peer.')
hwVoRecv_BRJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 18), Counter32()).setLabel("hwVoRecv-BRJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_BRJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_BRJ.setDescription('BRJ message number receive from peer.')
hwVoRecv_DRJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 19), Counter32()).setLabel("hwVoRecv-DRJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_DRJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_DRJ.setDescription('DRJ message number receive from peer.')
hwVoRecv_URQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 20), Counter32()).setLabel("hwVoRecv-URQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_URQ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_URQ.setDescription('URQ message number receive from peer.')
hwVoRecv_UCF = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 21), Counter32()).setLabel("hwVoRecv-UCF").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_UCF.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_UCF.setDescription('UCF message number receive from peer.')
hwVoRecv_URJ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 22), Counter32()).setLabel("hwVoRecv-URJ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_URJ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_URJ.setDescription('URJ message number receive from peer.')
hwVoRecv_IRQ = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 23), Counter32()).setLabel("hwVoRecv-IRQ").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_IRQ.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_IRQ.setDescription('IRQ message number receive from peer.')
hwVoRecv_UnknownRASMsg = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 11, 1, 3, 24), Counter32()).setLabel("hwVoRecv-UnknownRASMsg").setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoRecv_UnknownRASMsg.setStatus('current')
if mibBuilder.loadTexts: hwVoRecv_UnknownRASMsg.setDescription('Unknow ras message number receive from peer.')
mibBuilder.exportSymbols("HUAWEI-VO-H323-CALL-STAT-MIB", hwVoRecv_MSDReject=hwVoRecv_MSDReject, hwVoSend_FacilityTCSReject=hwVoSend_FacilityTCSReject, hwVoRecv_ARJ=hwVoRecv_ARJ, hwVoRecv_Alerting=hwVoRecv_Alerting, hwVoSend_FacilityOLCAck=hwVoSend_FacilityOLCAck, hwVoSend_IRR=hwVoSend_IRR, hwVoSend_BRQ=hwVoSend_BRQ, hwVoSend_Connect=hwVoSend_Connect, hwVoSend_CLCAck=hwVoSend_CLCAck, hwVoSend_OLCRequest=hwVoSend_OLCRequest, hwVoSend_FacilityCLCRequest=hwVoSend_FacilityCLCRequest, hwVoIPPRASStatObjects=hwVoIPPRASStatObjects, hwVoRecv_URJ=hwVoRecv_URJ, hwVoSend_MSDRequest=hwVoSend_MSDRequest, hwVoRecv_BCF=hwVoRecv_BCF, hwVoSend_MSDAck=hwVoSend_MSDAck, hwVoSend_FacilityCLCAck=hwVoSend_FacilityCLCAck, hwVoSend_FacilityMSDRequest=hwVoSend_FacilityMSDRequest, hwVoRecv_ReleaseComplete=hwVoRecv_ReleaseComplete, hwVoSend_ErrorH245Msg=hwVoSend_ErrorH245Msg, hwVoSend_RRQ=hwVoSend_RRQ, hwVoRecv_TCSReject=hwVoRecv_TCSReject, hwVoRecv_FacilityMSDReject=hwVoRecv_FacilityMSDReject, hwVoSend_FacilityOLCRequest=hwVoSend_FacilityOLCRequest, hwVoSend_FacilityIndUserInput=hwVoSend_FacilityIndUserInput, hwVoRecv_Progress=hwVoRecv_Progress, hwVoSend_FacilityTCSAck=hwVoSend_FacilityTCSAck, hwVoSend_FacilityTCSRequest=hwVoSend_FacilityTCSRequest, hwVoRecv_FacilityTCSReject=hwVoRecv_FacilityTCSReject, hwVoSend_TCSReject=hwVoSend_TCSReject, hwVoRecv_RCF=hwVoRecv_RCF, hwVoIPPH245StatObjects=hwVoIPPH245StatObjects, hwVoRecv_CallProceeding=hwVoRecv_CallProceeding, hwVoRecv_UnknownH225Msg=hwVoRecv_UnknownH225Msg, hwVoSend_DRQ=hwVoSend_DRQ, hwVoSend_UCF=hwVoSend_UCF, hwVoRecv_TCSAck=hwVoRecv_TCSAck, hwVoSend_CallProceeding=hwVoSend_CallProceeding, hwVoRecv_FacilityMSDAck=hwVoRecv_FacilityMSDAck, hwVoiceH323CallStatMIB=hwVoiceH323CallStatMIB, hwVoSend_ARQ=hwVoSend_ARQ, PYSNMP_MODULE_ID=hwVoiceH323CallStatMIB, hwVoRecv_MSDRequest=hwVoRecv_MSDRequest, hwVoSend_Setup=hwVoSend_Setup, hwVoSend_MSDReject=hwVoSend_MSDReject, hwVoRecv_GRJ=hwVoRecv_GRJ, hwVoRecv_BRJ=hwVoRecv_BRJ, hwVoSend_ErrorH225Msg=hwVoSend_ErrorH225Msg, hwVoSend_UserInput=hwVoSend_UserInput, hwVoIPPH225StatObjects=hwVoIPPH225StatObjects, hwVoRecv_FacilityOLCReject=hwVoRecv_FacilityOLCReject, hwVoRecv_FacilityOLCRequest=hwVoRecv_FacilityOLCRequest, hwVoRecv_TCSRequest=hwVoRecv_TCSRequest, hwVoSend_FacilityOLCReject=hwVoSend_FacilityOLCReject, hwVoRecv_UnknownH245Msg=hwVoRecv_UnknownH245Msg, hwVoRecv_OLCAck=hwVoRecv_OLCAck, hwVoSend_OLCReject=hwVoSend_OLCReject, hwVoSend_ErrorRASMsg=hwVoSend_ErrorRASMsg, hwVoRecv_URQ=hwVoRecv_URQ, hwVoRecv_FacilityCLCRequest=hwVoRecv_FacilityCLCRequest, hwVoRecv_DCF=hwVoRecv_DCF, hwVoRecv_CLCAck=hwVoRecv_CLCAck, hwVoRecv_CLCRequest=hwVoRecv_CLCRequest, hwVoSend_FacilityStartH245=hwVoSend_FacilityStartH245, hwVoRecv_OLCRequest=hwVoRecv_OLCRequest, hwVoSend_TCSAck=hwVoSend_TCSAck, hwVoRecv_FacilityMSDRequest=hwVoRecv_FacilityMSDRequest, hwVoRecv_IRQ=hwVoRecv_IRQ, hwVoRecv_Setup=hwVoRecv_Setup, hwVoRecv_FacilityTCSRequest=hwVoRecv_FacilityTCSRequest, hwVoRecv_ACF=hwVoRecv_ACF, hwVoRecv_UnknownRASMsg=hwVoRecv_UnknownRASMsg, hwVoRecv_MSDAck=hwVoRecv_MSDAck, hwVoRecv_GCF=hwVoRecv_GCF, hwVoSend_FacilityMSDAck=hwVoSend_FacilityMSDAck, hwVoSend_OLCAck=hwVoSend_OLCAck, hwVoSend_FacilityMSDReject=hwVoSend_FacilityMSDReject, hwVoRecv_UCF=hwVoRecv_UCF, hwVoRecv_FacilityCLCAck=hwVoRecv_FacilityCLCAck, hwVoSend_Alerting=hwVoSend_Alerting, hwVoSend_CLCRequest=hwVoSend_CLCRequest, hwVoRecv_RRJ=hwVoRecv_RRJ, hwVoSend_ReleaseComplete=hwVoSend_ReleaseComplete, hwVoRecv_Connect=hwVoRecv_Connect, hwVoRecv_UserInput=hwVoRecv_UserInput, hwVoH323CallStatObjects=hwVoH323CallStatObjects, hwVoSend_TCSRequest=hwVoSend_TCSRequest, hwVoRecv_OLCReject=hwVoRecv_OLCReject, hwVoSend_GRQ=hwVoSend_GRQ, hwVoRecv_FacilityOLCAck=hwVoRecv_FacilityOLCAck, hwVoSend_URQ=hwVoSend_URQ, hwVoRecv_FacilityTCSAck=hwVoRecv_FacilityTCSAck, hwVoRecv_DRJ=hwVoRecv_DRJ)
