#
# PySNMP MIB module ALCATEL-IND1-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:03:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Ssh, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Ssh")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Gauge32, Counter64, IpAddress, Bits, Integer32, ModuleIdentity, TimeTicks, NotificationType, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Counter64", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1))
alcatelIND1SshMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1SshMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setOrganization('Alcatel-Lucent')
alcatelIND1SshMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBObjects.setStatus('current')
alcatelIND1SshMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBConformance.setStatus('current')
alcatelIND1SshMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBGroups.setStatus('current')
alcatelIND1SshMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliances.setStatus('current')
alaSshAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshAdminStatus.setStatus('current')
alaScpSftpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaScpSftpAdminStatus.setStatus('current')
alaSshPubKeyEnforceAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPubKeyEnforceAdminStatus.setStatus('current')
alcatelIND1SshMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SshMIBCompliance = alcatelIND1SshMIBCompliance.setStatus('current')
alaSshConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 39, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaScpSftpAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaSshPubKeyEnforceAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaSshConfigGroup = alaSshConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SSH-MIB", alcatelIND1SshMIBGroups=alcatelIND1SshMIBGroups, alcatelIND1SshMIBCompliance=alcatelIND1SshMIBCompliance, alcatelIND1SshMIBConformance=alcatelIND1SshMIBConformance, alcatelIND1SshMIB=alcatelIND1SshMIB, PYSNMP_MODULE_ID=alcatelIND1SshMIB, alaSshConfigGroup=alaSshConfigGroup, alcatelIND1SshMIBObjects=alcatelIND1SshMIBObjects, alaSshPubKeyEnforceAdminStatus=alaSshPubKeyEnforceAdminStatus, alcatelIND1SshMIBCompliances=alcatelIND1SshMIBCompliances, alaScpSftpAdminStatus=alaScpSftpAdminStatus, alaSshAdminStatus=alaSshAdminStatus)
