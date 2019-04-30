#
# PySNMP MIB module NSLDAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSLDAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
DistinguishedName, applIndex, URLString = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "DistinguishedName", "applIndex", "URLString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, iso, MibIdentifier, Integer32, enterprises, ModuleIdentity, IpAddress, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, Gauge32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "Integer32", "enterprises", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType")
TextualConvention, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp")
netscape = MibIdentifier((1, 3, 6, 1, 4, 1, 1450))
nsldap = ModuleIdentity((1, 3, 6, 1, 4, 1, 1450, 7))
if mibBuilder.loadTexts: nsldap.setLastUpdated('9707310000Z')
if mibBuilder.loadTexts: nsldap.setOrganization('Netscape Communications Corp')
dsOpsTable = MibTable((1, 3, 6, 1, 4, 1, 1450, 7, 1), )
if mibBuilder.loadTexts: dsOpsTable.setStatus('current')
dsOpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsOpsEntry.setStatus('current')
dsAnonymousBinds = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsAnonymousBinds.setStatus('current')
dsUnAuthBinds = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsUnAuthBinds.setStatus('current')
dsSimpleAuthBinds = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSimpleAuthBinds.setStatus('current')
dsStrongAuthBinds = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsStrongAuthBinds.setStatus('current')
dsBindSecurityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsBindSecurityErrors.setStatus('current')
dsInOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsInOps.setStatus('current')
dsReadOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsReadOps.setStatus('current')
dsCompareOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCompareOps.setStatus('current')
dsAddEntryOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsAddEntryOps.setStatus('current')
dsRemoveEntryOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsRemoveEntryOps.setStatus('current')
dsModifyEntryOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsModifyEntryOps.setStatus('current')
dsModifyRDNOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsModifyRDNOps.setStatus('current')
dsListOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsListOps.setStatus('current')
dsSearchOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSearchOps.setStatus('current')
dsOneLevelSearchOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsOneLevelSearchOps.setStatus('current')
dsWholeSubtreeSearchOps = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsWholeSubtreeSearchOps.setStatus('current')
dsReferrals = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsReferrals.setStatus('current')
dsChainings = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsChainings.setStatus('current')
dsSecurityErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSecurityErrors.setStatus('current')
dsErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsErrors.setStatus('current')
dsEntriesTable = MibTable((1, 3, 6, 1, 4, 1, 1450, 7, 2), )
if mibBuilder.loadTexts: dsEntriesTable.setStatus('current')
dsEntriesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsEntriesEntry.setStatus('current')
dsMasterEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsMasterEntries.setStatus('current')
dsCopyEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCopyEntries.setStatus('current')
dsCacheEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheEntries.setStatus('current')
dsCacheHits = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsCacheHits.setStatus('current')
dsSlaveHits = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSlaveHits.setStatus('current')
dsIntTable = MibTable((1, 3, 6, 1, 4, 1, 1450, 7, 3), )
if mibBuilder.loadTexts: dsIntTable.setStatus('current')
dsIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "NSLDAP-MIB", "dsIntIndex"))
if mibBuilder.loadTexts: dsIntEntry.setStatus('current')
dsIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dsIntIndex.setStatus('current')
dsName = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 2), DistinguishedName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsName.setStatus('current')
dsTimeOfCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsTimeOfCreation.setStatus('current')
dsTimeOfLastAttempt = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsTimeOfLastAttempt.setStatus('current')
dsTimeOfLastSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsTimeOfLastSuccess.setStatus('current')
dsFailuresSinceLastSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsFailuresSinceLastSuccess.setStatus('current')
dsFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsFailures.setStatus('current')
dsSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsSuccesses.setStatus('current')
dsURL = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 3, 1, 9), URLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsURL.setStatus('current')
dsEntityTable = MibTable((1, 3, 6, 1, 4, 1, 1450, 7, 5), )
if mibBuilder.loadTexts: dsEntityTable.setStatus('current')
dsEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1), ).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"))
if mibBuilder.loadTexts: dsEntityEntry.setStatus('current')
dsEntityDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityDescr.setStatus('mandatory')
dsEntityVers = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityVers.setStatus('mandatory')
dsEntityOrg = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityOrg.setStatus('mandatory')
dsEntityLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityLocation.setStatus('mandatory')
dsEntityContact = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityContact.setStatus('mandatory')
dsEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1450, 7, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsEntityName.setStatus('mandatory')
nsDirectoryServerDown = NotificationType((1, 3, 6, 1, 4, 1, 1450) + (0,7001)).setObjects(("NSLDAP-MIB", "dsEntityDescr"), ("NSLDAP-MIB", "dsEntityVers"), ("NSLDAP-MIB", "dsEntityLocation"), ("NSLDAP-MIB", "dsEntityContact"))
nsDirectoryServerStart = NotificationType((1, 3, 6, 1, 4, 1, 1450) + (0,7002)).setObjects(("NSLDAP-MIB", "dsEntityDescr"), ("NSLDAP-MIB", "dsEntityVers"), ("NSLDAP-MIB", "dsEntityLocation"))
mibBuilder.exportSymbols("NSLDAP-MIB", dsSlaveHits=dsSlaveHits, dsEntityEntry=dsEntityEntry, dsFailures=dsFailures, dsAnonymousBinds=dsAnonymousBinds, dsEntityOrg=dsEntityOrg, dsUnAuthBinds=dsUnAuthBinds, dsModifyEntryOps=dsModifyEntryOps, dsBindSecurityErrors=dsBindSecurityErrors, dsAddEntryOps=dsAddEntryOps, dsReferrals=dsReferrals, nsDirectoryServerStart=nsDirectoryServerStart, dsListOps=dsListOps, dsWholeSubtreeSearchOps=dsWholeSubtreeSearchOps, dsCacheEntries=dsCacheEntries, dsCacheHits=dsCacheHits, dsSuccesses=dsSuccesses, dsInOps=dsInOps, dsIntIndex=dsIntIndex, dsURL=dsURL, dsTimeOfLastSuccess=dsTimeOfLastSuccess, netscape=netscape, dsEntityDescr=dsEntityDescr, dsEntriesEntry=dsEntriesEntry, PYSNMP_MODULE_ID=nsldap, dsSimpleAuthBinds=dsSimpleAuthBinds, dsName=dsName, dsReadOps=dsReadOps, nsDirectoryServerDown=nsDirectoryServerDown, dsEntityVers=dsEntityVers, dsOpsTable=dsOpsTable, dsEntityLocation=dsEntityLocation, dsEntityContact=dsEntityContact, dsFailuresSinceLastSuccess=dsFailuresSinceLastSuccess, dsEntityName=dsEntityName, nsldap=nsldap, dsStrongAuthBinds=dsStrongAuthBinds, dsSearchOps=dsSearchOps, dsMasterEntries=dsMasterEntries, dsChainings=dsChainings, dsTimeOfCreation=dsTimeOfCreation, dsCompareOps=dsCompareOps, dsSecurityErrors=dsSecurityErrors, dsOneLevelSearchOps=dsOneLevelSearchOps, dsIntTable=dsIntTable, dsTimeOfLastAttempt=dsTimeOfLastAttempt, dsEntityTable=dsEntityTable, dsOpsEntry=dsOpsEntry, dsErrors=dsErrors, dsModifyRDNOps=dsModifyRDNOps, dsIntEntry=dsIntEntry, dsRemoveEntryOps=dsRemoveEntryOps, dsEntriesTable=dsEntriesTable, dsCopyEntries=dsCopyEntries)