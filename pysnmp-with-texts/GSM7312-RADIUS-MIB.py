#
# PySNMP MIB module GSM7312-RADIUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7312-RADIUS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
gsm7312, = mibBuilder.importSymbols("GSM7312-REF-MIB", "gsm7312")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, ModuleIdentity, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, TimeTicks, Integer32, Bits, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "TimeTicks", "Integer32", "Bits", "IpAddress", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
gsm7312Radius = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8))
gsm7312Radius.setRevisions(('2003-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gsm7312Radius.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: gsm7312Radius.setLastUpdated('200305070000Z')
if mibBuilder.loadTexts: gsm7312Radius.setOrganization('Netgear')
if mibBuilder.loadTexts: gsm7312Radius.setContactInfo('')
if mibBuilder.loadTexts: gsm7312Radius.setDescription('The GSM7312 Radius MIB')
agentRadiusConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1))
agentRadiusMaxTransmit = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setStatus('current')
if mibBuilder.loadTexts: agentRadiusMaxTransmit.setDescription('Maximum number of retransmissions of a RADIUS request packet')
agentRadiusTimeout = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusTimeout.setStatus('current')
if mibBuilder.loadTexts: agentRadiusTimeout.setDescription('Time out duration (in seconds) before packets are retransmitted')
agentRadiusAccountingMode = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingMode.setDescription('Identifies if RADIUS Accounting has been enabled or not')
agentRadiusStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusStatsClear.setStatus('current')
if mibBuilder.loadTexts: agentRadiusStatsClear.setDescription('When set to enable(1), all Radius statistics will be reset.')
agentRadiusAccountingIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingIndexNextValid.setDescription('Indicates the next valid index into the agentRadiusAccountingConfigTable for creation. If no additional entries are allowed, this will be 0.')
agentRadiusAccountingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6), )
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingConfigTable.setDescription('Table with information about Radius Accounting Server IP Addresses, port numbers and shared secret. Only one entry is supported at this time.')
agentRadiusAccountingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1), ).setIndexNames((0, "GSM7312-RADIUS-MIB", "agentRadiusAccountingServerIndex"))
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingConfigEntry.setDescription('Entry consisting of configuration data for a Radius Accounting Server.')
agentRadiusAccountingServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerIndex.setDescription('Unique index of the configured RADIUS accounting server')
agentRadiusAccountingServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingServerAddress.setDescription('IP Address of the configured RADIUS accounting server. This object cannot be changed after creation.')
agentRadiusAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1813)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingPort.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingPort.setDescription('Port number for the RADIUS accounting server. This object cannot be configured on row creation.')
agentRadiusAccountingSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingSecret.setDescription('Configured shared sercret for the RADIUS accounting server. This object cannot be configured on row creation.')
agentRadiusAccountingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setStatus('current')
if mibBuilder.loadTexts: agentRadiusAccountingStatus.setDescription('')
agentRadiusServerIndexNextValid = MibScalar((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerIndexNextValid.setDescription('Indicates the next valid index into the agentRadiusServerConfigTable for creation. If no additional entries are allowed, this will be 0.')
agentRadiusServerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8), )
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerConfigTable.setDescription('Table with information about Radius Accounting Server IP Addresses, port numbers and shared secret')
agentRadiusServerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1), ).setIndexNames((0, "GSM7312-RADIUS-MIB", "agentRadiusServerIndex"))
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerConfigEntry.setDescription('Entry consisting of configuration data for a Radius Server. Creation requires setting ')
agentRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: agentRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerIndex.setDescription('Unique index of the configured RADIUS server')
agentRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerAddress.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerAddress.setDescription('IP Address of the configured RADIUS server. This object cannot be changed after creation.')
agentRadiusServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPort.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerPort.setDescription('Port number for the RADIUS server. This object cannot be configured on row creation.')
agentRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerSecret.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerSecret.setDescription('Configured shared sercret for the RADIUS server. This object cannot be configured on row creation.')
agentRadiusServerPrimaryMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerPrimaryMode.setDescription('Configure the RADIUS server to be the primary server. If there is any other server that is configured to be primary, that server is set to be a seconday server and this entry is set Primary. This object cannot be configured on row creation.')
agentRadiusServerCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerCurrentMode.setDescription('Indicate if the RADIUS server is the current server in user for authentication.')
agentRadiusServerMsgAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerMsgAuth.setDescription('Enable or disable the message authenticator attribute for this RADIUS server. This object cannot be configured on row creation.')
agentRadiusServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4526, 1, 6, 8, 1, 8, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentRadiusServerStatus.setStatus('current')
if mibBuilder.loadTexts: agentRadiusServerStatus.setDescription('')
mibBuilder.exportSymbols("GSM7312-RADIUS-MIB", agentRadiusAccountingPort=agentRadiusAccountingPort, agentRadiusServerAddress=agentRadiusServerAddress, agentRadiusStatsClear=agentRadiusStatsClear, agentRadiusAccountingStatus=agentRadiusAccountingStatus, agentRadiusServerIndex=agentRadiusServerIndex, agentRadiusServerSecret=agentRadiusServerSecret, agentRadiusConfigGroup=agentRadiusConfigGroup, agentRadiusAccountingConfigTable=agentRadiusAccountingConfigTable, agentRadiusAccountingMode=agentRadiusAccountingMode, agentRadiusAccountingServerAddress=agentRadiusAccountingServerAddress, agentRadiusMaxTransmit=agentRadiusMaxTransmit, agentRadiusServerConfigEntry=agentRadiusServerConfigEntry, agentRadiusServerPrimaryMode=agentRadiusServerPrimaryMode, agentRadiusServerConfigTable=agentRadiusServerConfigTable, gsm7312Radius=gsm7312Radius, agentRadiusServerStatus=agentRadiusServerStatus, agentRadiusServerCurrentMode=agentRadiusServerCurrentMode, PYSNMP_MODULE_ID=gsm7312Radius, agentRadiusTimeout=agentRadiusTimeout, agentRadiusAccountingSecret=agentRadiusAccountingSecret, agentRadiusServerPort=agentRadiusServerPort, agentRadiusServerIndexNextValid=agentRadiusServerIndexNextValid, agentRadiusServerMsgAuth=agentRadiusServerMsgAuth, agentRadiusAccountingConfigEntry=agentRadiusAccountingConfigEntry, agentRadiusAccountingIndexNextValid=agentRadiusAccountingIndexNextValid, agentRadiusAccountingServerIndex=agentRadiusAccountingServerIndex)
