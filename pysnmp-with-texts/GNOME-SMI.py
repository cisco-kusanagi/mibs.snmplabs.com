#
# PySNMP MIB module GNOME-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GNOME-SMI
# Produced by pysmi-0.3.4 at Wed May  1 13:19:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, TimeTicks, iso, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, enterprises, Counter32, Bits, ObjectIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "TimeTicks", "iso", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "enterprises", "Counter32", "Bits", "ObjectIdentity", "Gauge32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gnome = ModuleIdentity((1, 3, 6, 1, 4, 1, 3319))
gnome.setRevisions(('2007-09-07 00:00', '2005-05-07 00:00', '2003-12-07 00:00', '1998-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gnome.setRevisionsDescriptions(('Fixed wrong enterprise number (how comes this typo was unnoticed for so long?).', 'Added gnomeLDAP subtree for LDAP definitions.', 'Added gnomeSysadmin subtree for GNOME project system administration. Updated contact info.', 'Initial version.',))
if mibBuilder.loadTexts: gnome.setLastUpdated('200709070000Z')
if mibBuilder.loadTexts: gnome.setOrganization('GNOME project')
if mibBuilder.loadTexts: gnome.setContactInfo('GNU Network Object Model Environment project see http://www.gnome.org for contact persons of a particular area or subproject of GNOME. Administrative contact for MIB module: Jochen Friedrich Ramsaystr. 9 63450 Hanau Germany email: jochen@scram.de')
if mibBuilder.loadTexts: gnome.setDescription('The Structure of GNOME.')
gnomeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1))
if mibBuilder.loadTexts: gnomeProducts.setStatus('current')
if mibBuilder.loadTexts: gnomeProducts.setDescription('gnomeProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
gnomeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 2))
if mibBuilder.loadTexts: gnomeMgmt.setStatus('current')
if mibBuilder.loadTexts: gnomeMgmt.setDescription('gnomeMgmt defines the subtree for production GNOME related MIB registrations.')
gnomeTest = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 3))
if mibBuilder.loadTexts: gnomeTest.setStatus('current')
if mibBuilder.loadTexts: gnomeTest.setDescription('gnomeTest defines the subtree for testing GNOME related MIB registrations.')
gnomeSysadmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 4))
if mibBuilder.loadTexts: gnomeSysadmin.setStatus('current')
if mibBuilder.loadTexts: gnomeSysadmin.setDescription('gnomeSysadmin defines the subtree for GNOME related Sysadmin MIB registrations.')
gnomeLDAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 5))
if mibBuilder.loadTexts: gnomeLDAP.setStatus('current')
if mibBuilder.loadTexts: gnomeLDAP.setDescription('gnomeLDAP defines the subtree for GNOME related LDAP registrations.')
mibBuilder.exportSymbols("GNOME-SMI", gnomeMgmt=gnomeMgmt, gnomeSysadmin=gnomeSysadmin, gnomeTest=gnomeTest, gnomeLDAP=gnomeLDAP, PYSNMP_MODULE_ID=gnome, gnome=gnome, gnomeProducts=gnomeProducts)
