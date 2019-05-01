#
# PySNMP MIB module H3C-VOIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOIF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Gauge32, Unsigned32, TimeTicks, IpAddress, iso, Counter64, Integer32, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Gauge32", "Unsigned32", "TimeTicks", "IpAddress", "iso", "Counter64", "Integer32", "Counter32", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cVoiceIf = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2))
h3cVoiceIf.setRevisions(('2005-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVoiceIf.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cVoiceIf.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceIf.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cVoiceIf.setContactInfo('PLAT Team Huawei 3Com Technologies co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cVoiceIf.setDescription('This MIB file is to provide the definition of the voice interface general configuration.')
h3cVoIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1))
h3cVoIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1), )
if mibBuilder.loadTexts: h3cVoIfConfigTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfConfigTable.setDescription('The table contains configurable parameters for both analog voice interface and digital voice interface.')
h3cVoIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1), ).setIndexNames((0, "H3C-VOIF-MIB", "h3cVoIfCfgPortNumber"), (0, "H3C-VOIF-MIB", "h3cVoIfCfgGroupNumber"))
if mibBuilder.loadTexts: h3cVoIfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfConfigEntry.setDescription('The entry of voice interface table.')
h3cVoIfCfgPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cVoIfCfgPortNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgPortNumber.setDescription('The port number of voice interface.')
h3cVoIfCfgGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cVoIfCfgGroupNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgGroupNumber.setDescription('The group number of voice interface. For an analog interface, the value is 255.')
h3cVoIfCfgCngOn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgCngOn.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgCngOn.setDescription('This object indicates whether the silence gaps should be filled with background noise.')
h3cVoIfConfigInputGain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfConfigInputGain.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfConfigInputGain.setDescription('This object indicates the amount of gain added to the receiver side of the voice interface. Unit is 0.1 db.')
h3cVoIfConfigOutputGain = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfConfigOutputGain.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfConfigOutputGain.setDescription('This object indicates the amount of gain added to the send side of the voice interface. Unit is 0.1 db.')
h3cVoIfCfgEchoCancelSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgEchoCancelSwitch.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgEchoCancelSwitch.setDescription('This object indicates whether the echo cancellation is enabled.')
h3cVoIfCfgEchoCancellDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgEchoCancellDelay.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgEchoCancellDelay.setDescription("This object indicates the delay of the echo cancellation for the voice interface. This value couldn't be modified unless h3cVoIfCfgEchoCancelSwitch is enable. Unit is milliseconds.")
h3cVoIfCfgPlarNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgPlarNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgPlarNumber.setDescription('This object indicates the E.164 phone number for plar mode.')
h3cVoIfCfgDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgDescription.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgDescription.setDescription('This object indicates the description of voice interface')
h3cVoIfCfgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgStatus.setDescription('This object indicates the status of voice interface.')
h3cVoIfCfgCallingNumSubstRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgCallingNumSubstRule.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgCallingNumSubstRule.setDescription('This object indicates a calling number substitute rule.')
h3cVoIfCfgCalledNumSubstRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoIfCfgCalledNumSubstRule.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgCalledNumSubstRule.setDescription('This object indicates a called number substitute rule.')
h3cVoIfCfgSubLine = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 2, 1, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoIfCfgSubLine.setStatus('current')
if mibBuilder.loadTexts: h3cVoIfCfgSubLine.setDescription('This object indicates the port subscriber line name.')
mibBuilder.exportSymbols("H3C-VOIF-MIB", h3cVoiceIf=h3cVoiceIf, h3cVoIfCfgPlarNumber=h3cVoIfCfgPlarNumber, h3cVoIfCfgCalledNumSubstRule=h3cVoIfCfgCalledNumSubstRule, h3cVoIfConfigTable=h3cVoIfConfigTable, h3cVoIfCfgEchoCancelSwitch=h3cVoIfCfgEchoCancelSwitch, h3cVoIfConfigEntry=h3cVoIfConfigEntry, PYSNMP_MODULE_ID=h3cVoiceIf, h3cVoIfCfgEchoCancellDelay=h3cVoIfCfgEchoCancellDelay, h3cVoIfCfgStatus=h3cVoIfCfgStatus, h3cVoIfCfgGroupNumber=h3cVoIfCfgGroupNumber, h3cVoIfConfigOutputGain=h3cVoIfConfigOutputGain, h3cVoIfObjects=h3cVoIfObjects, h3cVoIfConfigInputGain=h3cVoIfConfigInputGain, h3cVoIfCfgPortNumber=h3cVoIfCfgPortNumber, h3cVoIfCfgDescription=h3cVoIfCfgDescription, h3cVoIfCfgSubLine=h3cVoIfCfgSubLine, h3cVoIfCfgCngOn=h3cVoIfCfgCngOn, h3cVoIfCfgCallingNumSubstRule=h3cVoIfCfgCallingNumSubstRule)