#
# PySNMP MIB module ASCEND-MIBIPFAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPFAX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, ModuleIdentity, ObjectIdentity, Counter64, Integer32, Bits, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Counter64", "Integer32", "Bits", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "IpAddress", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibipFaxProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 84))
mibipFaxProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 84, 1), )
if mibBuilder.loadTexts: mibipFaxProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfileTable.setDescription('A list of mibipFaxProfile profile entries.')
mibipFaxProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-Index-o"))
if mibBuilder.loadTexts: mibipFaxProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfileEntry.setDescription('A mibipFaxProfile entry containing objects that maps to the parameters of mibipFaxProfile profile.')
ipFaxProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 1), Integer32()).setLabel("ipFaxProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_Index_o.setDescription('')
ipFaxProfile_IpFaxEnabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipFaxProfile-IpFaxEnabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_IpFaxEnabled.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_IpFaxEnabled.setDescription('Enable IP Fax on this box ?')
ipFaxProfile_OutgoingFaxPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 3), Integer32()).setLabel("ipFaxProfile-OutgoingFaxPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_OutgoingFaxPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_OutgoingFaxPort.setDescription('TCP Port Number to listen on')
ipFaxProfile_ServerLogin = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 4), DisplayString()).setLabel("ipFaxProfile-ServerLogin").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_ServerLogin.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_ServerLogin.setDescription('Login name from Fax Server.')
ipFaxProfile_DialerType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mitel", 1), ("atlas", 2)))).setLabel("ipFaxProfile-DialerType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_DialerType.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_DialerType.setDescription('Set type of dialer use for incoming fax call.')
ipFaxProfile_ServerPassword = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 6), DisplayString()).setLabel("ipFaxProfile-ServerPassword").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_ServerPassword.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_ServerPassword.setDescription('Password from Fax Server.')
ipFaxProfile_IncomingFaxPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 7), Integer32()).setLabel("ipFaxProfile-IncomingFaxPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_IncomingFaxPort.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_IncomingFaxPort.setDescription('Port Number for Fax Server.')
ipFaxProfile_AllCallsAreFax = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipFaxProfile-AllCallsAreFax").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_AllCallsAreFax.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_AllCallsAreFax.setDescription('Enable IP Fax DNIS on incoming calls.')
ipFaxProfile_FaxIncomingCallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redialer", 1), ("did", 2)))).setLabel("ipFaxProfile-FaxIncomingCallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_FaxIncomingCallType.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxIncomingCallType.setDescription('Set type of incoming fax call.')
ipFaxProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ipFaxProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_Action_o.setDescription('')
mibipFaxProfile_FaxServersTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 84, 2), ).setLabel("mibipFaxProfile-FaxServersTable")
if mibBuilder.loadTexts: mibipFaxProfile_FaxServersTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxServersTable.setDescription('A list of mibipFaxProfile__fax_servers profile entries.')
mibipFaxProfile_FaxServersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1), ).setLabel("mibipFaxProfile-FaxServersEntry").setIndexNames((0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxServers-Index-o"), (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxServers-Index1-o"))
if mibBuilder.loadTexts: mibipFaxProfile_FaxServersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxServersEntry.setDescription('A mibipFaxProfile__fax_servers entry containing objects that maps to the parameters of mibipFaxProfile__fax_servers profile.')
ipFaxProfile_FaxServers_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 1), Integer32()).setLabel("ipFaxProfile-FaxServers-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxServers_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxServers_Index_o.setDescription('')
ipFaxProfile_FaxServers_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 2), Integer32()).setLabel("ipFaxProfile-FaxServers-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxServers_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxServers_Index1_o.setDescription('')
ipFaxProfile_FaxServers = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 2, 1, 3), IpAddress()).setLabel("ipFaxProfile-FaxServers").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_FaxServers.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxServers.setDescription('Fax Server addresses')
mibipFaxProfile_FaxDidTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 84, 3), ).setLabel("mibipFaxProfile-FaxDidTable")
if mibBuilder.loadTexts: mibipFaxProfile_FaxDidTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxDidTable.setDescription('A list of mibipFaxProfile__fax_did profile entries.')
mibipFaxProfile_FaxDidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1), ).setLabel("mibipFaxProfile-FaxDidEntry").setIndexNames((0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDid-Index-o"), (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDid-Index1-o"))
if mibBuilder.loadTexts: mibipFaxProfile_FaxDidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxDidEntry.setDescription('A mibipFaxProfile__fax_did entry containing objects that maps to the parameters of mibipFaxProfile__fax_did profile.')
ipFaxProfile_FaxDid_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 1), Integer32()).setLabel("ipFaxProfile-FaxDid-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxDid_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDid_Index_o.setDescription('')
ipFaxProfile_FaxDid_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 2), Integer32()).setLabel("ipFaxProfile-FaxDid-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxDid_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDid_Index1_o.setDescription('')
ipFaxProfile_FaxDid = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 3, 1, 3), DisplayString()).setLabel("ipFaxProfile-FaxDid").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_FaxDid.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDid.setDescription('List of DID Numbers for IP Fax facility.')
mibipFaxProfile_FaxDnisTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 84, 4), ).setLabel("mibipFaxProfile-FaxDnisTable")
if mibBuilder.loadTexts: mibipFaxProfile_FaxDnisTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxDnisTable.setDescription('A list of mibipFaxProfile__fax_dnis profile entries.')
mibipFaxProfile_FaxDnisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1), ).setLabel("mibipFaxProfile-FaxDnisEntry").setIndexNames((0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDnis-Index-o"), (0, "ASCEND-MIBIPFAX-MIB", "ipFaxProfile-FaxDnis-Index1-o"))
if mibBuilder.loadTexts: mibipFaxProfile_FaxDnisEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipFaxProfile_FaxDnisEntry.setDescription('A mibipFaxProfile__fax_dnis entry containing objects that maps to the parameters of mibipFaxProfile__fax_dnis profile.')
ipFaxProfile_FaxDnis_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 1), Integer32()).setLabel("ipFaxProfile-FaxDnis-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis_Index_o.setDescription('')
ipFaxProfile_FaxDnis_Index1_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 2), Integer32()).setLabel("ipFaxProfile-FaxDnis-Index1-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis_Index1_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis_Index1_o.setDescription('')
ipFaxProfile_FaxDnis = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 84, 4, 1, 3), DisplayString()).setLabel("ipFaxProfile-FaxDnis").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis.setStatus('mandatory')
if mibBuilder.loadTexts: ipFaxProfile_FaxDnis.setDescription('Dialed Number for IP Fax facility.')
mibBuilder.exportSymbols("ASCEND-MIBIPFAX-MIB", ipFaxProfile_FaxDnis_Index1_o=ipFaxProfile_FaxDnis_Index1_o, mibipFaxProfile_FaxDidTable=mibipFaxProfile_FaxDidTable, mibipFaxProfile_FaxDnisEntry=mibipFaxProfile_FaxDnisEntry, ipFaxProfile_IpFaxEnabled=ipFaxProfile_IpFaxEnabled, ipFaxProfile_DialerType=ipFaxProfile_DialerType, ipFaxProfile_FaxDid_Index_o=ipFaxProfile_FaxDid_Index_o, ipFaxProfile_FaxServers_Index1_o=ipFaxProfile_FaxServers_Index1_o, ipFaxProfile_ServerPassword=ipFaxProfile_ServerPassword, ipFaxProfile_FaxDid=ipFaxProfile_FaxDid, mibipFaxProfile_FaxServersEntry=mibipFaxProfile_FaxServersEntry, ipFaxProfile_FaxDnis=ipFaxProfile_FaxDnis, ipFaxProfile_FaxServers=ipFaxProfile_FaxServers, ipFaxProfile_AllCallsAreFax=ipFaxProfile_AllCallsAreFax, mibipFaxProfile_FaxDidEntry=mibipFaxProfile_FaxDidEntry, ipFaxProfile_Action_o=ipFaxProfile_Action_o, ipFaxProfile_Index_o=ipFaxProfile_Index_o, mibipFaxProfileEntry=mibipFaxProfileEntry, ipFaxProfile_FaxServers_Index_o=ipFaxProfile_FaxServers_Index_o, ipFaxProfile_FaxIncomingCallType=ipFaxProfile_FaxIncomingCallType, DisplayString=DisplayString, mibipFaxProfile_FaxServersTable=mibipFaxProfile_FaxServersTable, ipFaxProfile_FaxDid_Index1_o=ipFaxProfile_FaxDid_Index1_o, mibipFaxProfile=mibipFaxProfile, ipFaxProfile_OutgoingFaxPort=ipFaxProfile_OutgoingFaxPort, mibipFaxProfile_FaxDnisTable=mibipFaxProfile_FaxDnisTable, ipFaxProfile_FaxDnis_Index_o=ipFaxProfile_FaxDnis_Index_o, ipFaxProfile_ServerLogin=ipFaxProfile_ServerLogin, mibipFaxProfileTable=mibipFaxProfileTable, ipFaxProfile_IncomingFaxPort=ipFaxProfile_IncomingFaxPort)
