#
# PySNMP MIB module SUBSCRIBEEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUBSCRIBEEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
subscribeExt, = mibBuilder.importSymbols("APENT-MIB", "subscribeExt")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, IpAddress, Counter32, Counter64, ObjectIdentity, NotificationType, TimeTicks, Unsigned32, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apSubscribeExtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 58, 1))
if mibBuilder.loadTexts: apSubscribeExtMib.setLastUpdated('0006082000Z')
if mibBuilder.loadTexts: apSubscribeExtMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: apSubscribeExtMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: apSubscribeExtMib.setDescription('The MIB module used to describe the ArrowPoint Communications subscriber')
apSubTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2), )
if mibBuilder.loadTexts: apSubTable.setStatus('current')
if mibBuilder.loadTexts: apSubTable.setDescription('A list of Subscribers')
apSubEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1), ).setIndexNames((0, "SUBSCRIBEEXT-MIB", "apSubName"))
if mibBuilder.loadTexts: apSubEntry.setStatus('current')
if mibBuilder.loadTexts: apSubEntry.setDescription('A group of information uniqely identifying a subscriber.')
apSubName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubName.setStatus('current')
if mibBuilder.loadTexts: apSubName.setDescription('The name of the Subsriber service')
apSubState = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("accessFail", 0), ("ready", 1), ("busy", 2), ("busyRetry", 3), ("online", 4), ("suspended", 5), ("down", 6), ("initializing", 7), ("waitsConfig", 8), ("invalid", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubState.setStatus('current')
if mibBuilder.loadTexts: apSubState.setDescription('The status of our subscriber.')
apSubAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessError.setStatus('current')
if mibBuilder.loadTexts: apSubAccessError.setDescription('The error returned if apSubState is accessFail(0)')
apSubAccessIP = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessIP.setStatus('current')
if mibBuilder.loadTexts: apSubAccessIP.setDescription('The IP address of the publisher.')
apSubAccessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessUserName.setStatus('current')
if mibBuilder.loadTexts: apSubAccessUserName.setDescription('Usernmae to use when logging in to a publisher.')
apSubSubscribedFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubSubscribedFiles.setStatus('current')
if mibBuilder.loadTexts: apSubSubscribedFiles.setDescription('The total number of subscribed files.')
apSubLastMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubLastMethod.setStatus('current')
if mibBuilder.loadTexts: apSubLastMethod.setDescription('The last method of retrieval.')
apSubSynchronized = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubSynchronized.setStatus('current')
if mibBuilder.loadTexts: apSubSynchronized.setDescription("Is our subscriber sync'd with the server?")
apSubAccessType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ftp", 0), ("http", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessType.setStatus('current')
if mibBuilder.loadTexts: apSubAccessType.setDescription('The type of access to the publisher.')
apSubAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessPort.setStatus('current')
if mibBuilder.loadTexts: apSubAccessPort.setDescription('The port to access content on the publisher.')
apSubAccessBaseDir = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubAccessBaseDir.setStatus('current')
if mibBuilder.loadTexts: apSubAccessBaseDir.setDescription('The base directory to access content on the publisher.')
apSubSubscribedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubSubscribedBytes.setStatus('current')
if mibBuilder.loadTexts: apSubSubscribedBytes.setDescription('The total number of bytes received from a publisher.')
apSubLastTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 58, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apSubLastTime.setStatus('current')
if mibBuilder.loadTexts: apSubLastTime.setDescription('The last time we subscribed!')
mibBuilder.exportSymbols("SUBSCRIBEEXT-MIB", apSubLastMethod=apSubLastMethod, PYSNMP_MODULE_ID=apSubscribeExtMib, apSubAccessError=apSubAccessError, apSubTable=apSubTable, apSubSubscribedFiles=apSubSubscribedFiles, apSubLastTime=apSubLastTime, apSubState=apSubState, apSubAccessPort=apSubAccessPort, apSubAccessIP=apSubAccessIP, apSubSubscribedBytes=apSubSubscribedBytes, apSubscribeExtMib=apSubscribeExtMib, apSubName=apSubName, apSubEntry=apSubEntry, apSubAccessBaseDir=apSubAccessBaseDir, apSubAccessUserName=apSubAccessUserName, apSubSynchronized=apSubSynchronized, apSubAccessType=apSubAccessType)
