#
# PySNMP MIB module CISCO-DMN-DSG-LOCKLEVEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-LOCKLEVEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:55:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, TimeTicks, ObjectIdentity, Unsigned32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, MibIdentifier, Integer32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "MibIdentifier", "Integer32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGLockLevel = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22))
ciscoDSGLockLevel.setRevisions(('2010-08-30 11:00', '2010-06-28 06:00', '2010-05-24 06:30', '2009-12-20 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGLockLevel.setRevisionsDescriptions(('V01.00.03 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.02 2010-06-28 Updated the description for lockLevel.', 'V01.00.01 2010-05-24 Updated the options for lockLevel.', 'V01.00.00 2009-12-20 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGLockLevel.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGLockLevel.setDescription('Cisco Lock Level MIB.')
lockLevel = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevel.setStatus('current')
if mibBuilder.loadTexts: lockLevel.setDescription('Lock Level. (0) : All settings are unlocked. (1) : All settings are unlocked except Factory reset, IP settings and passwords. (2) : All settings are unlocked except that presets, tuning related items, and dish setup are also locked. (3) : All settings are locked except volume change. (4) : All settings are locked (can be changed via NC uplink signal only). four is a read-only value.')
lockLevelPWD = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWD.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWD.setDescription('Password to change Password and Lock Level.')
lockLevelPWDCUR = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCUR.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDCUR.setDescription('Confirm the Current Password.')
lockLevelPWDNEW = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDNEW.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDNEW.setDescription('New Password.')
lockLevelPWDCONF = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 22, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lockLevelPWDCONF.setStatus('current')
if mibBuilder.loadTexts: lockLevelPWDCONF.setDescription('Confirm New Password.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-LOCKLEVEL-MIB", lockLevelPWDCUR=lockLevelPWDCUR, lockLevel=lockLevel, lockLevelPWD=lockLevelPWD, PYSNMP_MODULE_ID=ciscoDSGLockLevel, lockLevelPWDNEW=lockLevelPWDNEW, lockLevelPWDCONF=lockLevelPWDCONF, ciscoDSGLockLevel=ciscoDSGLockLevel)
