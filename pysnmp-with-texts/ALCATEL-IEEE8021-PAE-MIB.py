#
# PySNMP MIB module ALCATEL-IEEE8021-PAE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IEEE8021-PAE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
dot1xAuthConfigEntry, = mibBuilder.importSymbols("IEEE8021-PAE-MIB", "dot1xAuthConfigEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, MibIdentifier, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, NotificationType, Integer32, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "NotificationType", "Integer32", "iso", "Gauge32", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
alcatelObjects, alcatelCommonMIBModules, alcatelConformance, alcatelNotifyPrefix = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "alcatelObjects", "alcatelCommonMIBModules", "alcatelConformance", "alcatelNotifyPrefix")
TPolicyStatementNameOrEmpty, ServiceAdminStatus, TNamedItem = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TPolicyStatementNameOrEmpty", "ServiceAdminStatus", "TNamedItem")
alcatelIEEE8021PaeMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 3))
alcatelIEEE8021PaeMIBModule.setRevisions(('1907-01-01 00:00', '1905-08-31 00:00', '1905-03-29 00:00', '1904-08-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIEEE8021PaeMIBModule.setRevisionsDescriptions(('Rev 5.0 01 Jan 2007 00:00 5.0 release of the ALCATEL-IEEE8021-PAE-MIB.', 'Rev 3.0 31 Aug 2005 00:00 3.0 release of the ALCATEL-IEEE8021-PAE-MIB.', 'Rev 2.0 29 Mar 2005 00:00 2.0 release of the ALCATEL-IEEE8021-PAE-MIB.', 'Rev 1.0 03 Aug 2004 00:00 1.0 release of the ALCATEL-IEEE8021-PAE-MIB.',))
if mibBuilder.loadTexts: alcatelIEEE8021PaeMIBModule.setLastUpdated('0701010000Z')
if mibBuilder.loadTexts: alcatelIEEE8021PaeMIBModule.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIEEE8021PaeMIBModule.setContactInfo('Alcatel-Lucent SROS Support Web: http://support.alcatel-lucent.com ')
if mibBuilder.loadTexts: alcatelIEEE8021PaeMIBModule.setDescription("This document is the SNMP MIB module to manage and provision the 7x50 extensions to the IEEE8021-PAE-MIB (Port Access Entity nodule for managing IEEE 802.X) feature for the Alcatel 7x50 device. Copyright 2004-2011 Alcatel-Lucent. All rights reserved. Reproduction of this document is authorized on the condition that the foregoing copyright notice is included. This SNMP MIB module (Specification) embodies Alcatel-Lucent's proprietary intellectual property. Alcatel-Lucent retains all title and ownership in the Specification, including any revisions. Alcatel-Lucent grants all interested parties a non-exclusive license to use and distribute an unmodified copy of this Specification in connection with management of Alcatel-Lucent products, and without fee, provided this copyright notice and license appear on all copies. This Specification is supplied 'as is', and Alcatel-Lucent makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
alxDot1xObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3))
alxDot1xAuthenticatorObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1))
alxDot1xRadiusObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2))
alxDot1xConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3))
alxDot1xAuthenticatorConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1))
alxDot1xAuthenticatorCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 1))
alxDot1xAuthenticatorGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 2))
alxDot1xRadiusConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2))
alxDot1xRadiusCompliancs = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 1))
alxDot1xRadiusGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 2))
alxDot1xNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 3))
alxDot1xNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 3, 0))
class AlxDot1xRadiusServerType(TextualConvention, Integer32):
    description = 'The AlxDot1xRadiusServerType data type is used to denote the type of the RADIUS server.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("authorization", 0), ("accounting", 1), ("combined", 2))

alxdot1xAuthConfigTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1), )
if mibBuilder.loadTexts: alxdot1xAuthConfigTable.setStatus('current')
if mibBuilder.loadTexts: alxdot1xAuthConfigTable.setDescription('The table alxdot1xAuthConfigTable allows configuration of RADIUS authentication parameters for the 802.1X PAE feature on port level.')
alxDot1xAuthConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1, 1), )
dot1xAuthConfigEntry.registerAugmentions(("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xAuthConfigEntry"))
alxDot1xAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
if mibBuilder.loadTexts: alxDot1xAuthConfigEntry.setStatus('current')
if mibBuilder.loadTexts: alxDot1xAuthConfigEntry.setDescription('alxDot1xAuthConfigEntry is an entry (conceptual row) in the alxdot1xAuthConfigTable. Each entry represents the configuration for Radius Authentication on a port. Entries have a presumed StorageType of nonVolatile.')
alxDot1xAuthRadiusPlcy = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1, 1, 50), TPolicyStatementNameOrEmpty()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alxDot1xAuthRadiusPlcy.setStatus('current')
if mibBuilder.loadTexts: alxDot1xAuthRadiusPlcy.setDescription('alxDot1xAuthRadiusPlcy specifies the name of the Radius Policy. The Radius Policy specifies the parameters that control the Radius Protocol. If no Policy is specified (empty string) no Radius authentication will be possible. This object can only be set to a policy that is defined in the alxdot1xRadiusServerPlcyTable.')
alxDot1xRadiusServerPlcyTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1), )
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyTable.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyTable.setDescription('The alxDot1xRadiusServerPlcyTable allows configuration of RADIUS authentication parameters for the 802.1X PAE feature.')
alxDot1xRadiusServerPlcyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyName"))
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyEntry.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyEntry.setDescription('alxDot1xRadiusServerPlcyEntry is an entry (conceptual row) in the alxDot1xRadiusServerPlcyTable. Each entry represents the configuration for a 802.1X Radius Policy. Entries in this table can be created and deleted via SNMP SET operations to alxDot1xRadiusPlcyRowStatus. Entries have a presumed StorageType of nonVolatile.')
alxDot1xRadiusPlcyName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 1), TNamedItem())
if mibBuilder.loadTexts: alxDot1xRadiusPlcyName.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyName.setDescription('The value of the object alxDot1xRadiusPlcyName specifies a specific radius server Policy to be used for 802.1X authentication.')
alxDot1xRadiusPlcySrceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusPlcySrceAddr.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcySrceAddr.setDescription('The value of the object alxDot1xRadiusPlcySrceAddr specifies the source address of the Radius packet. It must be a valid unicast address. (otherwise a wrongValue error is returned.) If this object is configured with the address of the router interface, the Radius client uses it while making a request to the server. If the address is not configured or is not the address of the one of interfaces, the source address is based on the address of the Radius server. If the server address is in-band, the client uses the system ip address. If it is out-of-band, the source address is the address of the management interface.')
alxDot1xRadiusPlcyAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 3), ServiceAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusPlcyAdminState.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyAdminState.setDescription('The value of the object alxDot1xRadiusPlcyAdminState specifies a specific radius server Policy to be used for 802.1x authentication.')
alxDot1xRadiusPlcyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusPlcyRowStatus.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyRowStatus.setDescription('alxDot1xRadiusPlcyRowStatus controls the creation and deletion of rows in the table.')
alxDot1xRadiusPlcyRetryAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusPlcyRetryAttempts.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyRetryAttempts.setDescription('The value of the object alxDot1xRadiusPlcyRetryAttempts specifies the number of RADIUS requests towards the same RADIUS server.')
alxDot1xRadiusPlcyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 90)).clone(5)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusPlcyTimeout.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyTimeout.setDescription('The value of alxDot1xRadiusPlcyTimeout specifies the time, in seconds, between request retries towards the same RADIUS server.')
alxDot1xRadiusServerTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2), )
if mibBuilder.loadTexts: alxDot1xRadiusServerTable.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerTable.setDescription('The alxDot1xRadiusServerTable has an entry for each RADIUS server used for 802.1x authentication.')
alxDot1xRadiusServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1), ).setIndexNames((0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerPlcyName"), (0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerIndex"))
if mibBuilder.loadTexts: alxDot1xRadiusServerEntry.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerEntry.setDescription('alxDot1xRadiusServerEntry is an entry (conceptual row) in the alxDot1xRadiusServerTable. Each entry represents the configuration for a RADIUS server. Entries in this table can be created and deleted via SNMP SET operations on alxDot1xRadiusServerRowStatus.')
alxDot1xRadiusServerPlcyName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 1), TNamedItem())
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyName.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerPlcyName.setDescription('The value of the object alxDot1xRadiusServerPlcyName specifies the radius server Policy to be used for 802.1x authentication as defined in the alxDot1xRadiusServerPlcyTable. Row creation will be denied if no policy with the same name does not occur in the alxDot1xRadiusServerPlcyTable.')
alxDot1xRadiusServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: alxDot1xRadiusServerIndex.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerIndex.setDescription('The value of the object alxDot1xRadiusServerIndex specifies a specific radius server in the policy.')
alxDot1xRadiusServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerAddress.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerAddress.setDescription('The value of the object alxDot1xRadiusServerAddress specifies the IP address of the RADIUS server. A valid unicast IP address must be specified for row creation to succeed.')
alxDot1xRadiusServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerSecret.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerSecret.setDescription('The value of the object alxDot1xRadiusServerSecret specifies the secret key associated with the RADIUS server. An Empty key is not accepted.')
alxDot1xRadiusServerAuthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerAuthPort.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerAuthPort.setDescription('The value of the object alxDot1xRadiusServerAuthPort specifies the UDP port number on which to contact the RADIUS server for authentication.')
alxDot1xRadiusServerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alxDot1xRadiusServerOperStatus.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerOperStatus.setDescription('The value of the object alxDot1xRadiusServerOperStatus indicates the current status of the RADIUS server.')
alxDot1xRadiusServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerRowStatus.setDescription('alxDot1xRadiusServerRowStatus controls the creation and deletion of rows in the table.')
alxDot1xRadiusServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 8), AlxDot1xRadiusServerType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerType.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerType.setDescription('The value of the object alxDot1xRadiusServerType indicates the type of the RADIUS server.')
alxDot1xRadiusServerAcctPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1813)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alxDot1xRadiusServerAcctPort.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusServerAcctPort.setDescription('The value of the object alxDot1xRadiusServerAcctPort specifies the UDP port number on which to contact the RADIUS server for accounting.')
alxDot1xAuthConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 2, 1)).setObjects(("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xAuthRadiusPlcy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alxDot1xAuthConfigGroup = alxDot1xAuthConfigGroup.setStatus('current')
if mibBuilder.loadTexts: alxDot1xAuthConfigGroup.setDescription('The group of objects supporting management of Radius authentication for the IEEE801.1X PAE feature on Alcatel 7x50 SR series systems.')
alxDot1xRadiusPlcyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 2, 1)).setObjects(("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcySrceAddr"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyAdminState"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyRowStatus"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyRetryAttempts"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyTimeout"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAddress"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerSecret"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAuthPort"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAcctPort"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerOperStatus"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerRowStatus"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alxDot1xRadiusPlcyGroup = alxDot1xRadiusPlcyGroup.setStatus('current')
if mibBuilder.loadTexts: alxDot1xRadiusPlcyGroup.setDescription('The group of objects supporting management of Radius authentication for the IEEE801.1X PAE feature on Alcatel 7x50 SR series systems.')
alxDot1xAuthenticatorCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 1, 1)).setObjects(("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xAuthConfigGroup"), ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alxDot1xAuthenticatorCompliance = alxDot1xAuthenticatorCompliance.setStatus('current')
if mibBuilder.loadTexts: alxDot1xAuthenticatorCompliance.setDescription('The compliance statement for management of Radius authentication for the IEEE801.1X PAE feature on Alcatel 7x50 SR series systems.')
mibBuilder.exportSymbols("ALCATEL-IEEE8021-PAE-MIB", alxDot1xRadiusServerPlcyEntry=alxDot1xRadiusServerPlcyEntry, alxDot1xRadiusPlcySrceAddr=alxDot1xRadiusPlcySrceAddr, alxDot1xRadiusPlcyRowStatus=alxDot1xRadiusPlcyRowStatus, alxDot1xObjs=alxDot1xObjs, alxDot1xAuthRadiusPlcy=alxDot1xAuthRadiusPlcy, alxDot1xRadiusServerOperStatus=alxDot1xRadiusServerOperStatus, alxDot1xRadiusServerAuthPort=alxDot1xRadiusServerAuthPort, alxDot1xAuthenticatorConformance=alxDot1xAuthenticatorConformance, alxDot1xAuthenticatorObjs=alxDot1xAuthenticatorObjs, alxDot1xAuthConfigGroup=alxDot1xAuthConfigGroup, alxDot1xRadiusPlcyTimeout=alxDot1xRadiusPlcyTimeout, alxdot1xAuthConfigTable=alxdot1xAuthConfigTable, alxDot1xRadiusCompliancs=alxDot1xRadiusCompliancs, alxDot1xNotifications=alxDot1xNotifications, AlxDot1xRadiusServerType=AlxDot1xRadiusServerType, alxDot1xConformance=alxDot1xConformance, alxDot1xRadiusServerType=alxDot1xRadiusServerType, alxDot1xAuthenticatorCompliance=alxDot1xAuthenticatorCompliance, alxDot1xRadiusGroups=alxDot1xRadiusGroups, alxDot1xRadiusPlcyAdminState=alxDot1xRadiusPlcyAdminState, alxDot1xRadiusServerRowStatus=alxDot1xRadiusServerRowStatus, alcatelIEEE8021PaeMIBModule=alcatelIEEE8021PaeMIBModule, alxDot1xAuthConfigEntry=alxDot1xAuthConfigEntry, alxDot1xRadiusServerEntry=alxDot1xRadiusServerEntry, alxDot1xRadiusServerAddress=alxDot1xRadiusServerAddress, alxDot1xRadiusPlcyGroup=alxDot1xRadiusPlcyGroup, alxDot1xRadiusServerIndex=alxDot1xRadiusServerIndex, alxDot1xRadiusObjs=alxDot1xRadiusObjs, alxDot1xAuthenticatorCompliancs=alxDot1xAuthenticatorCompliancs, alxDot1xRadiusServerSecret=alxDot1xRadiusServerSecret, alxDot1xRadiusServerTable=alxDot1xRadiusServerTable, alxDot1xNotificationsPrefix=alxDot1xNotificationsPrefix, alxDot1xAuthenticatorGroups=alxDot1xAuthenticatorGroups, PYSNMP_MODULE_ID=alcatelIEEE8021PaeMIBModule, alxDot1xRadiusServerPlcyTable=alxDot1xRadiusServerPlcyTable, alxDot1xRadiusPlcyName=alxDot1xRadiusPlcyName, alxDot1xRadiusServerAcctPort=alxDot1xRadiusServerAcctPort, alxDot1xRadiusServerPlcyName=alxDot1xRadiusServerPlcyName, alxDot1xRadiusPlcyRetryAttempts=alxDot1xRadiusPlcyRetryAttempts, alxDot1xRadiusConformance=alxDot1xRadiusConformance)
